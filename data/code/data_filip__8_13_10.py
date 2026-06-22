def parse_csv_generator(data):
    for item in data.split(','):
        stripped = item.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    sample_input = "apple,  banana , ,cherry,  ,  date  "
    result = list(parse_csv_generator(sample_input))
    print(result)