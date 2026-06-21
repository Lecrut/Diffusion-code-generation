numbers_dict = {
    "evens": [],
    "odds": []
}

def filter_numbers(numbers):
    numbers_dict["evens"] = list(filter(lambda x: x % 2 == 0, numbers))
    numbers_dict["odds"] = list(filter(lambda x: x % 2 != 0, numbers))

if __name__ == '__main__':
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_numbers(input_list)
    print(numbers_dict["evens"])
    print(numbers_dict["odds"])