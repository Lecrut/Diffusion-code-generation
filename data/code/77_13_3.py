import sys
def convert_time_to_minutes(h, m, s):
    total_minutes = h * 60 + m + s / 60
    return total_minutes
if __name__ == '__main__':
    sample_input = "1:30:15"
    try:
        parts = sample_input.split(':')
        if len(parts) != 3:
            print("Error: Input format must be Hours:Minutes:Seconds")
            sys.exit(1)
        h = int(parts[0])
        m = int(parts[1])
        s = int(parts[2])
        if h < 0 or m < 0 or s < 0 or m >= 60 or s >= 60:
            print("Error: Invalid time values. Minutes and Seconds must be between 0 and 59.")
            sys.exit(1)
        total_minutes = convert_time_to_minutes(h, m, s)
        print(f"{total_minutes:.2f}")
    except ValueError:
        print("Error: All parts of the input must be integers.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)