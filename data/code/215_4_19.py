MAX_NUMBER = 50

def find_largest_number(data):
    return max(data.values())

if __name__ == '__main__':
    sample_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': MAX_NUMBER}
    print(f"Largest number: {find_largest_number(sample_dict)}")