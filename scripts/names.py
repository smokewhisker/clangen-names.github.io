import random
import os
import platform


class Name(object):
    special_suffixes = {
        "kitten": "kit",
        "apprentice": "paw",
        "medicine cat apprentice": "paw",
        "leader": "star"
    }
    normal_suffixes = [  # common suffixes
        "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", "fur", 'fur', 'fur', 'fur',
        'pelt', "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt", "pelt",
        "tail", "tail", "tail", "tail", "tail", "tail", "tail", "tail", "claw", "claw", "claw", "claw", "claw", "claw", "claw",
        "foot","foot", "foot","foot", "foot", "whisker", "whisker", "whisker", "whisker", "whisker", "whisker",
        "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", "heart", 'heart',

        # regular suffixes
        "bee", "belly", "berry", "bird", "blaze",
        "blossom", "bounce", "branch", "breeze", "briar", "bright", "brook", "burr", "bush",
        "call", "cloud", "creek", "dapple", "daisy", "dawn", "drop",
        "dusk", "dust", "ear", "ears", "eye", "eyes", "face", "fall", "fang", "feather", "fern", "fire",
        "fish", "flame", "flight", "flower", "frost", "goose", "gorse", "grass", 
        "hawk", "heather", "jaw",
         "leaf", "leap", "leg", "light", "lilac", "lily", "mask", "mist",
        "moon", "night", "nose", "patch",
        "petal", "pool", "poppy", "pounce", "puddle", "rose", "runner",
        "scar", "shade", "shadow", "shine", "skip", "sky", "slip", "snow", "song", 
        "spark", "speck", "speckle", "splash", "spot", "spots", "spring", "stalk", "stem", "step",
        "stone", "storm", "stream", "strike", "stripe", "sun",
        "tail", "throat", "tuft", "watcher", "water", "whisper", "willow", "wind", "wing", "wish"
    ]

    pelt_suffixes = {
        'TwoColour': ['patch', 'spot', 'splash', 'patch', 'spots'],
        'Tabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Marbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade'],
        'Speckled': ['dapple', 'speckle', 'spot', 'speck', 'freckle'],
        'Bengal': ['dapple', 'speckle', 'spots', 'speck', 'freckle'],
        'Tortie': ['dapple', 'speckle', 'spot', 'dapple'],
        'Rosette': ['dapple', 'speckle', 'spots', 'dapple'],
        'Calico': ['stripe', 'dapple', 'patch', 'patch'],
        'Smoke': [
'dusk', 'dawn'],
        'Ticked': ['spots', 'pelt', 'speckle'],
    }

    tortie_pelt_suffixes = {
        'tortiesolid': ['dapple', 'speckle', 'spots', 'splash'],
        'tortietabby': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortiebengal': ['dapple', 'speckle', 'spots', 'speck', 'fern', 'freckle'],
        'tortiemarbled': ['stripe', 'feather', 'leaf', 'stripe', 'shade', 'fern'],
        'tortieticked': ['spots', 'pelt', 'speckle'],
        'tortiesmoke': ['dusk', 'dawn'],
        'tortierosette': ['dapple', 'speckle', 'spots', 'dapple', 'fern' ],
        'tortiespeckled': ['dapple', 'speckle', 'spot', 'speck']
    }

    normal_prefixes = [
        'Acorn', 'Adder', 'Alder', 'Almond', 'Aloe',
        'Amber', 'Ant', 'Apple', 'Apricot', 'Arch', 
        'Ash', 'Aspen', 'Badger', 'Bark',
         'Basil', 'Bat', 'Bay', 
        'Bee', 'Beech', 'Beetle', 'Berry', 'Birch',
        'Bird', 'Blaze', 
        'Bloom', 'Blossom', 
        'Borage' 'Boulder', 'Bounce', 'Bracken', 'Bramble',
        'Branch', 'Brave', 'Breeze', 'Breeze', 'Briar', 'Bright', 'Brindle',
        'Bristle', 'Broken', 'Brook', 'Brush', 
        'Bumble','Burr', 'Bush', 'Buzzard',
        'Cedar', 'Cedar', 'Cherry',      
        'Chestnut', 'Chive', 'Cinder', 'Claw', 
        'Cloud', 'Clover', 'Clover',
        'Copper', 'Cotton',
         'Creek', 
        'Cricket', 'Crooked', 'Crouch', 'Crow', 'Crow', 
        'Cypress', 'Daisy', 'Dapple',
        'Dark', 'Dawn', 'Dawn', 'Deer', 'Dew', 'Doe', 'Dog',
        'Dove', 'Drift',
        'Duck', 'Dusk', 'Dust', 'Eagle', 'Echo', 'Eel',
        'Egret', 'Elk', 'Ember', 
        'Falcon', 'Fallow', 'Fawn', 'Feather', 'Fennel',
        'Fern', 'Ferret', 'Fidget', 'Fierce', 'Finch', 'Fish',
        'Flail', 'Flame', 'Flash', 'Fleck', 'Fleet', 
        'Flint', 'Flower', 'Flower',
        'Flutter', 'Fly', 'Forest', 'Fox', 'Freckle',
         'Frog', 'Frost', 
        'Fuzzy', 
      'Goose', 'Gorse', 'Grass', 'Gravel', 'Grouse',
        'Hail', 'Half', 'Hare', 'Hawk', 'Hay',
        'Heather', 'Heavy', 'Heron', 'Hickory',
        'Hollow', 'Holly'
        'Hound', 'Ice', 'Ivy', 'Jagged', 'Jay', 
         'Juniper', 'Kestrel', 'Lake', 'Larch', 'Lark',
         'Lavender', 'Leaf', 'Leopard', 'Lichen', 'Light',
        'Lightning', 'Lilac', 'Lilac', 'Lily', 'Little', 'Lizard', 'Locust',
        'Log', 'Long', 'Loud', 'Lynx', 'Maggot',
        'Mallow', 'Maple', 'Marigold', 'Marsh', 'Meadow',
        'Mellow', 'Midge', 'Milk', 'Minnow', 'Mint', 'Mist',
        'Mistle', 'Misty', 'Mole', 'Mole',
        'Morning', 'Moss', 'Moth', 'Moth', 'Mottle',
        'Mouse', 'Mouse', 'Mud', 'Mumble',
         'Nettle', 'Newt', 'Night', 'Nut', 'Oak', 'Oat','One',
         'Osprey', 'Otter', 'Owl', 'Pale', 
        'Parsley', 'Patch', 'Pear', 
        'Pebble', 'Perch', 'Petal', 'Pigeon', 'Pike',
        'Pine', 'Pond', 'Pool', 'Poppy', 
        'Pounce', 'Prickle', 'Puddle', 'Quail',
        'Quick', 'Quiet', 'Rabbit', 'Ragged', 'Rain',
         'Rat', 'Raven', 'Reed', 'Ridge',
        'Ripple', 'River', 'Robin', 'Rock', 'Rook', 'Root', 'Rose',
        'Swan', 'Rubble', 'Running', 'Rush','Rye',
        'Sage', 'Scar', 'Scorch', 'Sedge', 'Seed', 'Shade',
        'Sharp', 'Shell', 'Shimmer', 'Short', 'Shrew', 'Shy',
         'Sky', 'Slate', 'Sleek', 'Sleet', 'Slight', 'Sloe',
        'Small', 'Smoke', 'Snail', 'Snake',
         'Soft', 'Soot', 'Sorrel', 'Spark', 'Sparrow',
        'Speckle', 'Spider', 'Spike', 'Splash', 'Spotted', 'Spring',
        'Spruce', 'Squirrel', 'Stag', 'Starling', 'Stoat', 'Stone',
        'Storm', 'Stream', 'Swallow',
        'Swan', 'Sweet', 'Swift', 'Tall', 'Talon', 'Thistle', 'Thorn',
         'Thyme', 'Tiger', 'Timber', 'Toad', 'Trout',
         'Tulip', 'Tumble', 'Turtle', 'Twig', 'Vine', 'Violet', 'Vixen',
        'Vole', 'Wasp', 'Weasel', 'Web', 
        'Wild', 'Willow', 'Wind', 'Wolf', 'Wood',
        'Wren', 'Yarrow', 'Yew'
    ]

    colour_prefixes = {
        'WHITE': [
            'White', 'White', 'Pale', 'Snow', 'Cloud', 'Milk', 'Hail', 'Frost',
            'Ice', 'Sheep', 'Blizzard', 'Light'
        ],
        'PALEGREY': [
            'Gray', 'Silver', 'Pale', 'Cloud', 'Hail', 'Frost', 'Ice', 'Mouse',
            'Bright', "Fog"
        ],
        'SILVER': [
            'Gray', 'Silver', 'Cinder', 'Ice', 'Frost', 'Rain', 'Blue',
            'River', 'Blizzard'
        ],
        'GREY': [
            'Gray', 'Gray', 'Ash', 'Cinder', 'Rock', 'Stone', 'Shade', 'Mouse',
            'Smoke', 'Shadow', "Fog",
        ],
        'DARKGREY': [
            'Gray', 'Shade', 'Raven', 'Crow', 'Stone', 'Dark', 'Night',
            'Smoke', 'Shadow'
        ],
        'BLACK': [
            'Black', 'Black', 'Shade', 'Crow', 'Raven', 'Ebony', 'Dark',
            'Night', 'Shadow', 'Scorch'
        ],
        'PALEGINGER': [
            'Sand', 'Yellow', 'Pale', 'Sun', 'Light', 'Lion', 'Bright',
            'Honey', 'Daisy'
        ],
        'GOLDEN': [
            'Golden', 'Yellow', 'Sun', 'Light', 'Lightning', 'Thunder',
            'Honey', 'Tawny', 'Lion', 'Dandelion'
        ],
        'GINGER': [
            'Red', 'Fire', 'Flame', 'Ember', 'Sun', 'Light', 'Rose',
            'Rowan', 'Fox', 'Tawny', "Plum"
        ],
        'DARKGINGER': [
            'Red', 'Red', 'Fire', 'Flame', 'Oak', 'Shade', 'Russet',
            'Rowan', 'Fox'
        ],
        'LIGHTBROWN': [
            'Brown', 'Pale', 'Light', 'Mouse', 'Dust', 'Sand', 'Bright', 'Mud',
            'Hazel'
        ],
        'BROWN': [
            'Brown', 'Oak', 'Mouse', 'Dark', 'Shade', 'Russet', 'Stag',
            'Acorn', 'Mud', "Deer"
        ],
        'DARKBROWN':
        ['Brown', 'Shade', 'Dark', 'Night', 'Russet', 'Rowan', 'Mud']
    }

    eye_prefixes = {
        'YELLOW': ['Yellow', 'Daisy', 'Honey', 'Light'],
        'AMBER': ['Amber', 'Sun', 'Fire', 'Honey', 'Scorch'],
        'HAZEL': ['Tawny', 'Hazel', 'Daisy', 'Sand'],
        'PALEGREEN': ['Green', 'Pale', 'Mint', 'Fern', 'Weed'],
        'GREEN': ['Green', 'Fern', 'Weed', 'Holly', 'Clover', 'Olive'],
        'BLUE': ['Blue', 'Blue', 'Ice', 'Sky', 'Lake', 'Frost', 'Water'],
        'DARKBLUE': ['Blue', 'Sky', 'Lake', 'Berry', 'Dark', 'Water',],
        'BLUEYELLOW': ['Yellow', 'Blue', 'Odd', 'One'],
        'BLUEGREEN': ['Green', 'Blue', 'Odd', 'One', 'Clover']
    }

    loner_names = [
        "Haku", "Pichi", "Poki", "Nagi", "Jubie", "Bonbon", "Beans", "Aurora",
        "Maleficent", "Luna", "Eclipse", "Sol", "Star", "George", "Nightmare",
        "Bagel", "Monster", "Gargoyle", "Missile Launcher", "Rolo", "Rocket",
        "Void", "Abyss", "Vox", "Princess", "Noodle", "Duchess", "Cheesecake",
        "Callie", "Randy", "Ace", "Queeny", "Freddy", "Stella", "Rooster",
        "Sophie", "Maverick", "Seamus", 'Meowyman', "Pickles", "Lacy", "Lucy",
        "Knox", "Lugnut", "Bailey", "Azula", "Lucky", "Sunny", "Sadie", "Sox",
        "Bandit", "Onyx", "Quinn", "Grace", "Fang", "Ike", "Flower",
        "Whiskers", "Gust", "Peony", 'Human', "Minnie", "Buddy", "Mollie",
        "Jaxon", "Dunnock", "Firefly", "Cheese", "Sandwich", "Spam",
        'Brocolli', "Prickle", "Insect", "Grasshopper", "Coral", "Windy",
        "Sofa", "McChicken", "Katy Purry", 'Mop', "Fishtail", "Roman",
        "Wishbone", "Nova", "Quimby", "Quest", "Nessie", "Niles", "Neil",
        "Nutella", "Nakeena", "Nuka", "Hughie", "Harvey", "Herc", "French",
        "Finch", "Frannie", "Flutie", 'Purdy', "Free", "Glory", "Snek", "Indi",
        "Igor", "Jupiter", "Nintendo", "Jesse", "James", "Jethro", 'Shampoo',
        "Joker", "Jinx", "Chaos", "Havoc", "Trouble", "Kingston", "King",
        "Kip", "Kong", "Ken", "Kendra", "Kisha", "Kermit", "Kelloggs",
        "Kodiak", "Klondike", "Ketchup", "KD", "Lupo", "Luigi", "Lily", "Lora",
        "Lee", "Lex", "Lester", "Makwa", "Madi", "Minna", "Moxie", "Mucha",
        "Manda", "Monte", 'Riya', "Monzi", "Nisha", "Nemo", "Nitro", "Oops",
        "O'Leary", "Ophelia", "Olga", "Oscar", "Owen", "Porsche", "Ping",
        "Pong", "Quinzee", "Quickie", "Quagmire", "Quake", "Quinoa", "Roomba",
        "Riot", "Peanut Wigglebutt", "Ramble", "Rudolph", "Rum", "Reese",
        "Scotch", "Sneakers", "Schmidt", "Espresso", "Cocoa Puff", "Sonic",
        "Teufel", "Toni", "Toque", "Tempest", "Turbo", "Tetris", "Triscuit",
        "Tumble", "Voltage", "Vinnie", "Vaxx", "Venture", "Vida", "Guinness",
        "Polly", "Piper", "Pepper", "Lakota", "Dakota", "Bently", "Chinook",
        "Tiny", "Ula", "Union", "Uriel", "Orion", "Oakley", "Roselies",
        "Belle", "Benny", "Bumblebee", "Bluebell", "Chip", "Chocolate",
        "Cracker", "Dave", "Dolly", "Egg", "Frito", "Frank", "Gibby", "Jack",
        "Jenny", "Juliet", "Joob", "John", "Jimmy", "Jude", "Kenny", "Tom",
        "Oreo", "Mocha", "Ninja", "Cinderblock", "Pip", "Pipsqueak", "Milque",
        "Toast", "Molly Murder Mittens", "Flabby", "Crunchy", "Sorbet",
        "Vanilla", "Mint", "Niki", "Nikki", "Pocket", "Tabbytha", "Gravy",
        "Potato", "Chewy", "Pumpernickel", "Pecan", "Old Man Sam", "Icecube",
        "Queso Ruby", "Pearl", "Jasper", "Stan", "Rose", "Mojo", "Kate",
        "Carmen", "Mange", "Chase", "Socks", "Tabby", "Jay", "Charlie", "L",
        "Poopy", "Crunchwrap", "Meow-meow", "Bede", "Smores", "Evilface",
        "Nick", "Mitski", "Ash", "Ah", "Violet", "Alcina", "Worm", "Monika",
        "Rat", "Bongo", "Bunny", "Viktor", "Steve", "Jewels", "Blu", "Rue",
        "Stinky", "Garnet", "Anita", "Sloane", "Emi", "Vivienne", "Amber",
        "Moon", "Twilight", "River", "Glass", "Goose", "Hunter", "Amity",
        "Stripes", "Cowbell", "Rory", "Lobster", "Slug", "Starfish", "Salmon",
        "Judy", "Johnny", "Kerry", "Evelyn", "Holly", "Bolt", "Millie",
        "Jessica", "Laku", "Dragonfly", "X’ek", "Silva", "Dreamy", "Decay",
        "Twister", "Shay", "Louis", "Oleander", "Spots", "Cream", "Omlet",
        "Gizmo", "Feather", "Twix", "Silver", "Ghost", "Wisp", "Obi Wan",
        'Pikachu', "Mango", "Via", "Olivia", "Mr. Whiskers", "Fluffy",
        "Shimmer", "Mimi", "Melody", "Leon", "Punk", "Mew", "Fern",
        "Marceline", "Whisper", "Skrunkly", "Stolas", "Rio", "Steven", "Pear",
        "Sekhmet", "Mellon", "Ember", "Loona", "Saki", "Tiny", "Sandy",
        "Miles", "Mini", "Judas", "Zim", "Vinyl", "Rarity", "Trixie", "Sunset",
        "Anubis", "Armin", "Amy", "Alice", "Alec", "Baphomet", "Bean",
        "Bastet", "Birb", "Burm", "Chrissy", "Cherry", "Chief", "Crow",
        "Carrie", "Calvin", "Cookie", "Catie", "Charm", "Crab", "Charles",
        "Caroline", "Conan", "Cloud", "Charlie", "Cowboy", 'Burger', "Dune",
        "Dan", "Delilah", "Emerald", "Emy", "Erica", " Eddie", "Eda", "Ferret",
        "Fawn", "Fiver", "Fallow", "Ferry", "Gamble", "Grain", "Gir", "Hop",
        "Hot Sauce", "Habanero", "Taco Bell", "Cheetoman"
    ]

    if not platform.window.localStorage.getItem('prefixlist.txt') == None:
        name_list = platform.window.localStorage.getItem('prefixlist.txt')
        if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_prefixes.append(new_name)

    if not platform.window.localStorage.getItem('suffixlist.txt') == None:
        name_list = platform.window.localStorage.getItem('suffixlist.txt')
        if_names = len(name_list)
        if if_names > 0:
            new_names = name_list.split('\n')
            for new_name in new_names:
                if new_name != '':
                    normal_suffixes.append(new_name)

    def __init__(self,
                 status="warrior",
                 prefix=None,
                 suffix=None,
                 colour=None,
                 eyes=None,
                 pelt=None):
        self.status = status
        if prefix is None:
            if colour is None and eyes is None:
                self.prefix = random.choice(self.normal_prefixes)
            elif eyes is None:
                a = random.randint(0, 5)
                if a != 1:
                    self.prefix = random.choice(self.normal_prefixes)
                else:
                    self.prefix = random.choice(self.colour_prefixes[colour])
            elif colour is None:
                a = random.randint(0, 5)
                if a != 1:
                    self.prefix = random.choice(self.normal_prefixes)
                else:
                    self.prefix = random.choice(self.eye_prefixes[eyes])
            else:
                a = random.randint(0, 7)
                if a == 1:
                    self.prefix = random.choice(self.colour_prefixes[colour])
                elif a == 2:
                    self.prefix = random.choice(self.eye_prefixes[eyes])
                else:
                    self.prefix = random.choice(self.normal_prefixes)
        else:
            self.prefix = prefix
        if suffix is None:
            loop = True
            while loop:
                if pelt is None or pelt == 'SingleColour':
                    self.suffix = random.choice(self.normal_suffixes)
                else:
                    a = random.randint(0, 7)
                    if a == 1:
                        self.suffix = random.choice(self.pelt_suffixes[pelt])
                    elif a == 1 and self.pelt.name in ["Tortie", "Calico"]:
                        self.suffix = random.choice(self.tortie_pelt_suffixes)
                    else:
                        self.suffix = random.choice(self.normal_suffixes)
                if self.suffix != self.prefix.lower():
                    loop = False
        else:
            self.suffix = suffix

    def __repr__(self):
        if self.status in ["deputy", "warrior", "medicine cat", "elder"]:
            return self.prefix + self.suffix
        else:
            return self.prefix + self.special_suffixes[self.status]


names = Name()
