def convert_to_ml(liters):
    return liters * 1000

def main():
    test_cases = [1, 2.5, 10, 0.5, 0.1]
    results = list(map(convert_to_ml, test_cases))
    print(results)

if __name__ == '__main__':
    main()