class DictExtremes:
    def __init__(self, data: dict):
        self.data = data

    def calculate_difference(self) -> int:
        if not self.data:
            raise ValueError("Dictionary cannot be empty.")
        return max(self.data.values()) - min(self.data.values())

if __name__ == '__main__':
    sample_dict_1 = {'a': 5, 'b': 3, 'c': 9}
    extremes_instance_1 = DictExtremes(sample_dict_1)
    result_1 = extremes_instance_1.calculate_difference()
    print(f"Dictionary: {sample_dict_1}")
    print(f"Difference of extremes: {result_1}")

    sample_dict_2 = {'x': -2, 'y': 7, 'z': 0}
    extremes_instance_2 = DictExtremes(sample_dict_2)
    result_2 = extremes_instance_2.calculate_difference()
    print(f"\nDictionary: {sample_dict_2}")
    print(f"Difference of extremes: {result_2}")

    sample_dict_3 = {'m': 100, 'n': -50}
    extremes_instance_3 = DictExtremes(sample_dict_3)
    result_3 = extremes_instance_3.calculate_difference()
    print(f"\nDictionary: {sample_dict_3}")
    print(f"Difference of extremes: {result_3}")