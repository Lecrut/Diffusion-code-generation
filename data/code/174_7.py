def filter_phonebook(phonebook):
    filtered_phonebook = {}
    for name, phone_number in phonebook.items():
        if phone_number.startswith('5'):
            filtered_phonebook[name] = phone_number
    return filtered_phonebook
if __name__ == '__main__':
    sample_phonebook = {
        "Alice": "555-1234",
        "Bob": "555-5678",
        "Charlie": "555-9012",
        "David": "555-3456",
        "Eve": "555-0000"
    }
    result = filter_phonebook(sample_phonebook)
    print(result)