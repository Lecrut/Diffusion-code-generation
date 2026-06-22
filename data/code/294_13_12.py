class ObjectWeightCalculator:

    @staticmethod
    def calculate_equivalent_weight(mass, volume):
        if volume == 0:
            return None
        return mass / volume

    @classmethod
    def compare_weights(cls, obj1, obj2):
        eqw1 = cls.calculate_equivalent_weight(*obj1)
        eqw2 = cls.calculate_equivalent_weight(*obj2)
        if eqw1 is None or eqw2 is None:
            return None
        return (eqw1, eqw2)

    @staticmethod
    def find_heaviest_object(objects):
        max_eqw = float('-inf')
        heaviest_obj = None
        for obj in objects:
            eqw = cls.calculate_equivalent_weight(*obj)
            if eqw is not None and eqw > max_eqw:
                max_eqw = eqw
                heaviest_obj = obj
        return heaviest_obj
if __name__ == '__main__':
    object1 = (50, 2)
    object2 = (75, 3)
    eqw1, eqw2 = ObjectWeightCalculator.compare_weights(object1, object2)
    print(f'Equivalent weight of object1: {eqw1}, object2: {eqw2}')
    heaviest_obj = ObjectWeightCalculator.find_heaviest_object([object1, object2])
    print(f'Heaviest object: {heaviest_obj}')