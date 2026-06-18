def compare_distances(value1, unit1, value2, unit2):
    return f"{value1} {unit1} vs {value2} {unit2}"
if __name__ == '__main__':
    print(compare_distances(5.0, "km", 3000.0, "m"))