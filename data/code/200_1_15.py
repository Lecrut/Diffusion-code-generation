class StringProcessor:
    def process_strings(self, strings):
        return (s.strip().lower() for s in strings)

if __name__ == '__main__':
    processor = StringProcessor()
    sample_values = ["  Hello World  ", "Python Programming", "  Data Science  "]
    processed_values = list(processor.process_strings(sample_values))
    print(processed_values)