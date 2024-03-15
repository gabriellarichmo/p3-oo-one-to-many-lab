class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type.lower() not in self.PET_TYPES:
            raise ValueError("Invalid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        type(self).all.append(self)


class Owner:

    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return[pet for pet in Pet.all if isinstance(pet, Pet) and pet.owner == self]

    def add_pet(self, pet):
        #!Checks that the pet is type of Pet and adds the owner to the pet
        if not isinstance(pet, Pet):
            raise TypeError("The argument must be an instance of the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        #!Sorted list of pets by name
        return sorted(self.pets(), key=lambda pet: pet.name)
