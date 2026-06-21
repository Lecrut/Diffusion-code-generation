def filter_valid_weights(weight_measurements):
    def is_positive_number(s):
        try:
            return float(s) > 0
        except ValueError:
            return False

    return [float(w) for w in weight_measurements if is_positive_number(w)]

if __name__ == '__main__':
    sample_weights = ["50.3", "-25", "175", "def", "60.75", "0", "49.99"]
    print(filter_valid_weights(sample_weights))