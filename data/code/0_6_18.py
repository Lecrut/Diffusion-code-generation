import sys

def meters_to_yards(meters: float) -> float:
    """Convert a length from meters to yards."""
    return meters * 0.91440256

def read_lengths_from_file(filename: str):
    """Read lengths (in meters) from the specified file and yield them one by one."""
    with open(filename, 'r') as f:
        for line in f:
            try:
                length = float(line.strip())
                if length > 0:
                    yield length
            except ValueError:
                continue

def main():
    """Main function to execute the conversion script."""
    # Hard-coded sample values representing a list of lengths in meters.
    input_file_content = "1.5\n3.2\n4876.0"

    filename = 'input_lengths.txt'

    try:
        for meters in read_lengths_from_file(filename):
            yards = meters_to_yards(meters)
            print(f"{meters} m -> {yards:.4f} yd")
    except FileNotFoundError:
        # Since the actual file doesn't exist, we simulate using sample data directly.
        print("Using hard-coded samples because input file is not provided.")

        for meters_str in input_file_content.splitlines():
            if meters_str.strip() == "":
                continue
            try:
                meters = float(meters_str)
                yards = meters_to_yards(meters)
                print(f"{meters} m -> {yards:.4f} yd")
            except ValueError:
                continue

if __name__ == '__main__':
    main()