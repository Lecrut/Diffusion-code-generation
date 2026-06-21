lookup_list = ["one", "two", "three", "four", "five"]

def initialize_dictionary(start, end):
    return {i: lookup_list[i % len(lookup_list)] for i in range(start, end)}

if __name__ == '__main__':
    result_dict = initialize_dictionary(1, 10)
    print(result_dict)