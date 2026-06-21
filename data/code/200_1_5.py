class StringProcessor:
    @staticmethod
    def process_strings(strings):
        return (s.strip().lower() for s in strings)

if __name__ == '__main__':
    sample_values = ["  Python ", "PROGRAMMING", "  Data Science  ", "Machine LEARNING"]
    processor = StringProcessor()
    processed_values = list(processor.process_strings(sample_values))
    print(processed_values)