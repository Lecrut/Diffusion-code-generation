def process_file(filename):
    item_lengths = {}
    try:
        with open(filename, 'r') as file:
            item_names = file.readlines()
            for line in item_names:
                item_name = line.strip()
                if item_name:
                    item_lengths[item_name] = len(item_name)
    except FileNotFoundError:
        return item_lengths
    return item_lengths
if __name__ == '__main__':
    sample_data = [
        "apple\n",
        "banana\n",
        "kiwi\n",
        "orange\n"
    ]
    filename = "items.txt"
    with open(filename, 'w') as f:
        f.writelines(sample_data)
    result = process_file(filename)
    print(result)