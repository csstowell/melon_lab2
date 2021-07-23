############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code   
        self.first_harvest = first_harvest 
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        
        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list.
        """
        #append to self.pairings

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        new_code = self.code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        1998,
        "green",
        False,
        True, 
        "Muskmelon"
    )

    musk.add_pairing("Pairs well with mint")
    


    cas = MelonType(
        "cas",
        2003,
        "orange",
        True,
        None,
        "Casaba"

    )
    cas.add_pairing("Pairs well with strawberry and mint")
    
    cren = MelonType(
        "cren",
        1996,
        "green",
        None,
        None,
        "Crenshaw"
    )
    cren.add_pairing("Pairs well with prosciutto")

    yw = MelonType(
        "yw",
        2013,
        "yellow",
        True,
        True,
        "Yellow Watermelon"
    )
    yw.add_pairing("Pairs well with ice cream")

    all_melon_types.append(musk)
    all_melon_types.append(cas)
    all_melon_types.append(cren) 
    all_melon_types.append(yw)
    
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
# No return statement needed 
# loop through all melon types
# for each melon type -- print 
# Muskmelon pairs with
# - mint

    # Loop through melon in list melon_types
    for melon in melon_types:

        # .name assigns self.name to each melon in loop
        print(f'{melon.name} pairs with:')
        # Attached method to melon from above for loop
        for pairing in melon.pairings:
            print(f'- {pairing}')



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
# Dictionary that returns reporting codes as strings
# and whose values are the appropriate melon type instance for that reporting code.
# make a loop to loop through melons in melon_types
# for each melon, print code 
# creating the key melon_codes[melon.code] = melon.name
# key = melon.code
# value = melon.name
# melon_codes = key: value
    
    # Created an empty dictionary
    melon_codes = {}
    # Loop through list of melon types created by make_melon_types()
    for melon in melon_types:
        # Add to melon_codes dictionary with key=melon.code and value=melon
        melon_codes[melon.code] = melon
        # melon_codes = (melon.code, melon_codes) 

    return melon_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    # arguments melon instance assigned those as attributes
    
    def __init__(self, melon_type, shape, color_rating, harvest_from, harvest_by):
        """Initialize a Melon object"""
        self.melon_type = melon_type
        self.shape = shape
        self.color_rating = color_rating
        self.harvest_from = harvest_from
        self.harvest_by = harvest_by

    
    def is_sellable(self):
        if self.shape > 5 and self.color_rating > 5 and self.harvest_by != 3:
            return True

    #returns True or False
# able to be sold if both its shape and color ratings are greater than 5
# and if it didn’t come from field 3, which was found to have poisonous fertilizer planted by a competing melon farm

    
    
    
    
#    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
#                  name):
#         """Initialize a melon."""
#         self.code = code   
#         self.first_harvest = first_harvest 
#         self.color = color
#         self.is_seedless = is_seedless
#         self.is_bestseller = is_bestseller
#         self.name = name



    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""
# Make a list that instantiates a bunch of melons
# Make an empty list to populate

    melons = []

    melons_by_id = make_melon_type_lookup(melon_types)

    # Make a melon object:
    # (melon_type, shape, color_rating, harvest_from, harvest_by



    melon1 = Melon(
            melons_by_id['yw'],
            8,
            7,
            2,
            'Sheila', 
        )

    melon2 = Melon(
        melons_by_id['yw'],
        3,
        4,
        2,
        'Sheilaa'   
    )

    melon3 = Melon(
        melons_by_id['yw'],
        9,
        8,
        3,
        'Sheila'
    )


    melon4 = Melon(
        melons_by_id['yw'],
        10,
        6,
        35,
        'Sheila'
    )

    melon5 = Melon(
        melons_by_id['yw'],
        8,
        9,
        35,
        'Michael'
    )

    melon6 = Melon(
        melons_by_id['yw'],
        8,
        2,
        35,
        'Michael'
    )

    melon7 = Melon(
        melons_by_id['yw'],
        2,
        3,
        4,
        'Michael'
    )


    melon8 = Melon(
        melons_by_id['yw'],
        6,
        7,
        4,
        'Michael'
    )

    melon9 = Melon(
        melons_by_id['yw'],
        7,
        10,
        3,
        'Sheila'
    )

    melons = melons.extend([melon1, melon2, melon3, melon4, melon5, melon6, melon7, melon8, melon9])

    return melons
   

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
# prints out info about each melon about where it was harvested and sellable
    # Fill in the rest 


















































############
# Part 1   #
############

# class MelonType(object):
#     """A species of melon at a melon farm."""

#     def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
#                  name):
#         """Initialize a melon."""

#         self.pairings = []

#         # Fill in the rest

#     def add_pairing(self, pairing):
#         """Add a food pairing to the instance's pairings list."""

#         # Fill in the rest

#     def update_code(self, new_code):
#         """Replace the reporting code with the new_code."""

#         # Fill in the rest


# def make_melon_types():
#     """Returns a list of current melon types."""

#     all_melon_types = []

#     # Fill in the rest

#     return all_melon_types

# def print_pairing_info(melon_types):
#     """Prints information about each melon type's pairings."""

#     # Fill in the rest

# def make_melon_type_lookup(melon_types):
#     """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

#     # Fill in the rest

# ############
# # Part 2   #
# ############

# class Melon(object):
#     """A melon in a melon harvest."""

#     # Fill in the rest
#     # Needs __init__ and is_sellable methods

# def make_melons(melon_types):
#     """Returns a list of Melon objects."""

#     # Fill in the rest

# def get_sellability_report(melons):
#     """Given a list of melon object, prints whether each one is sellable."""

#     # Fill in the rest 



