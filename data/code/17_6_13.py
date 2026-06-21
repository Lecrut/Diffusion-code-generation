def retrieve_tail_element(sequence):
    last_index = -1
    return sequence[last_index]

if __name__ == '__main__':
    fruit_inventory = ['apple', 'banana', 'cherry', 'date']
    extracted_item = retrieve_tail_element(fruit_inventory)
    print(extracted_item)