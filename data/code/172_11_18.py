FruitWords = {
    1: 'apple',
    2: 'banana'
}

VegetableWords = {
    3: 'carrot',
    4: 'broccoli'
}

DairyWords = {
    5: 'milk'
}

def convert_keys_to_words(keys):
    result = {}
    for key in keys:
        if key in FruitWords:
            result[key] = FruitWords[key]
        elif key in VegetableWords:
            result[key] = VegetableWords[key]
        elif key in DairyWords:
            result[key] = DairyWords[key]
        else:
            result[key] = 'unknown'
    return result

if __name__ == '__main__':
    sample_keys = [1, 2, 3, 4, 5, 6]
    print(convert_keys_to_words(sample_keys))