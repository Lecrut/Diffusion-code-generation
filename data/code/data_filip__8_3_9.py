def split_and_filter(s):
    return list(filter(lambda x: x.strip() != '', s.split(',')))

if __name__ == '__main__':
    sample_input = "apple, banana, ,  ,orange, ,grape"
    print(split_and_filter(sample_input))