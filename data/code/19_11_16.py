import secrets

def get_random_element(values):
    if not values:
        return None
    index = secrets.randbelow(len(values))
    return values[index]

if __name__ == '__main__':
    sample_list = [1.2, 3.4, 5.6, 7.8, 9.0, 2.1, 4.3, 6.5, 8.7, 0.9]
    result = get_random_element(sample_list)
    print(result)