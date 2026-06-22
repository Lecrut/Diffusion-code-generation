def iterate_and_print(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")

if __name__ == '__main__':
    sample_dict = {'apple': 50, 'banana': 30, 'cherry': 20}
    iterate_and_print(sample_dict)