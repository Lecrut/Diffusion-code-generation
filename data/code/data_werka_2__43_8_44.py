def compute_area_of_square(side_length):
    return side_length ** 2

if __name__ == '__main__':
    sample_config = {'dimension': 5}
    print(compute_area_of_square(sample_config['dimension']))