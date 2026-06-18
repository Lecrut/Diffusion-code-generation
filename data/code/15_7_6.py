def main():
    # Sample dictionary with various keys
    data = {
        'key_a': 10,
        'key_b': 20,
        'key_c': 30,
        'key_d': 40,
        'key_e': 50,
        'key_f': 60,
    }

    # Define the two specific keys to compare
    key1 = 'key_a'
    key2 = 'key_b'

    # Dictionary comprehension: includes only items where values for both keys exist and are identical.
    # Note: Since a single dictionary cannot have duplicate keys with different values, 
    # this logic checks if the value at one specific key equals another specific key's value.
    result_dict = {key1 + '_' + key2: data[key1] == data[key2]}

    return result_dict

if __name__ == '__main__':
    output = main()
    print("Comparison Result:", output)