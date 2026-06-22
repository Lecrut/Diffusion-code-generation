class CSVParser:
    @staticmethod
    def parse_and_find_max(csv_string):
        if not csv_string.strip():
            raise ValueError("Empty CSV string")
        
        numbers = [int(num) for num in csv_string.split(',')]
        return max(numbers)

if __name__ == '__main__':
    sample_csv = "10,5,20,3"
    result = CSVParser.parse_and_find_max(sample_csv)
    print(result)