import numpy as np

def convert_volumes(input_array, from_unit, to_unit):
    conversions_to_ml = {'ml': 1.0, 'l': 1000.0, 'gal': 3785.411784, 'fl_oz': 29.5735295625, 'cup': 236.5882365, 'tbsp': 14.78676478125, 'tsp': 4.92892159375}
    input_array = np.asarray(input_array, dtype=float)
    from_factor = conversions_to_ml[from_unit]
    to_factor = conversions_to_ml[to_unit]
    converted = input_array * from_factor / to_factor
    return converted
if __name__ == '__main__':
    volumes_ml = np.array([100, 250, 500, 1000, 2500])
    converted_gal = convert_volumes(volumes_ml, 'ml', 'gal')
    print(converted_gal)
    volumes_gal = np.array([1, 2.5, 5, 10])
    converted_l = convert_volumes(volumes_gal, 'gal', 'l')
    print(converted_l)
    volumes_cup = np.array([1, 2, 4, 8])
    converted_tbsp = convert_volumes(volumes_cup, 'cup', 'tbsp')
    print(converted_tbsp)