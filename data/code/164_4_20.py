class AnimalGrouper:
    LEG_GROUPS = {2: 'birds', 4: 'quadrupeds', 8: 'octopuses'}

    def __init__(self):
        self.grouped_animals = {group: [] for group in self.LEG_GROUPS.values()}

    @staticmethod
    def _get_leg_group(legs):
        if legs == 2:
            return 'birds'
        elif legs == 4:
            return 'quadrupeds'
        elif legs == 8:
            return 'octopuses'
        else:
            raise ValueError(f"Unsupported number of legs: {legs}")

    def add_animal(self, animal, legs):
        leg_group = self._get_leg_group(legs)
        if leg_group in self.grouped_animals:
            self.grouped_animals[leg_group].append(animal)

    def get_grouped_animals(self):
        return self.grouped_animals

if __name__ == '__main__':
    grouper = AnimalGrouper()
    sample_animals = {
        "dog": 4,
        "cat": 4,
        "spider": 8,
        "ant": 6,
        "bird": 2
    }
    for animal, legs in sample_animals.items():
        grouper.add_animal(animal, legs)
    print(grouper.get_grouped_animals())