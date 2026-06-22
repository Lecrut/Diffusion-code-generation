def weight_difference_generator(weight_pairs):
    def calculate_difference(pair):
        return abs(pair[0] - pair[1])
    
    for pair in weight_pairs:
        yield calculate_difference(pair)

if __name__ == '__main__':
    SAMPLE_WEIGHT_PAIRS = [(75, 70), (82, 88), (93, 93)]
    differences = list(weight_difference_generator(SAMPLE_WEIGHT_PAIRS))
    print(differences)