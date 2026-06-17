def convert_to_pounds(filename):
    conversion_factor = 453.592
    pounds_values = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    mass_value = float(line.strip())
                    pounds = mass_value * conversion_factor
                    pounds_values.append(pounds)
                except ValueError:
                    continue
    except FileNotFoundError:
        return None
    return pounds_values
if __name__ == '__main__':
    sample_filename = "mass_data.txt"
    try:
        with open(sample_filename, 'w') as f:
            f.write("10.0\n")
            f.write("5.5\n")
            f.write("20.0\n")
            f.write("invalid_data\n")
            f.write("-3.2\n")
        results = convert_to_pounds(sample_filename)
        if results is not None:
            print("Mass values converted to pounds:")
            for lb in results:
                print(lb)
    except Exception as e:
        print(f"An error occurred during file setup or processing: {e}")