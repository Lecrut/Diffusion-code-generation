def convert_mass_to_pounds(filename):
    mass_values = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    mass_str = line.strip()
                    if mass_str:
                        mass_value = float(mass_str)
                        pounds_value = mass_value * 453.592
                        mass_values.append((mass_str, pounds_value))
                except ValueError:
                    continue
    except FileNotFoundError:
        return None
    except IOError:
        return None
    return mass_values
if __name__ == '__main__':
    sample_filename = "mass_data.txt"
    with open(sample_filename, 'w') as f:
        f.write("10.0\n")
        f.write("5.5\n")
        f.write("20.0\n")
        f.write("invalid_data\n")
        f.write("\n")
    results = convert_mass_to_pounds(sample_filename)
    if results is not None:
        print("Mass values converted to pounds:")
        for original, pounds in results:
            print(f"Original: {original}, Pounds: {pounds:.2f}")
    else:
        print("Error reading file or file not found.")