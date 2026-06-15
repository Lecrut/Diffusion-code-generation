def filter_phonebook(phonebook):
    result = {}
    for name, phone_number in phonebook.items():
        if phone_number.startswith('5'):
            result[name] = phone_number
    return result
if __name__ == '__main__':
    sample_phonebook = {
        "Alice": "555-1234",
        "Bob": "555-5678",
        "Charlie": "555-9012",
        "David": "555-3456",
        "Eve": "123-4567"
    }
    filtered_phonebook = filter_phonebook(sample_phonebook)
    print(filtered_phonebook)