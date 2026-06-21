def get_first_element(lst):
    ACCESS_KEYS = {
        'start': 0,
        'begin': 0
    }
    return lst[ACCESS_KEYS['start']]

if __name__ == '__main__':
    fruits = ["kiwi", "mango", "papaya"]
    print(get_first_element(fruits))