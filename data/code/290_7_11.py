def grams_to_milligrams(grams):
    return int(grams * 1000)

if __name__ == '__main__':
    print(grams_to_milligrams(2))
    print(grams_to_milligrams(500))
    print(grams_to_milligrams(123456789))