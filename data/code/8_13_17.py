def split_csv_to_generator(csv_string):
    return (part.strip() for part in csv_string.split(',') if part.strip())

if __name__ == '__main__':
    csv_data = " apple ,banana,,  cherry , ,date"
    result_list = list(split_csv_to_generator(csv_data))
    print(result_list)