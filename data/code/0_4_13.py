class LengthConverter:
    FACTOR = 1.0936132983

    def __init__(self):
        self.results = []

    def convert_value(self, meters):
        return meters * self.FACTOR

    def process_line(self, line):
        stripped = line.strip()
        if not stripped:
            return None
        try:
            value = float(stripped)
            converted = self.convert_value(value)
            self.results.append(converted)
            return converted
        except ValueError:
            self.results.append(0.0)
            return None

    def process_list(self, lines):
        converted_list = []
        for line in lines:
            result = self.process_line(line)
            if result is not None:
                converted_list.append(result)
        return converted_list

def simulate_file_content():
    temp_content = [
        "1.0",
        "2.5",
        "invalid",
        "10.0",
        "0.5",
        "   ",
        "15.55"
    ]
    return temp_content

if __name__ == '__main__':
    converter = LengthConverter()
    sample_lines = simulate_file_content()
    output_values = converter.process_list(sample_lines)
    for val in output_values:
        print(val)