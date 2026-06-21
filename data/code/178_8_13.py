class CSVParser:
    def parse_csv_first_column(self, csv_text):
        lines = csv_text.strip().split('\n')
        result = []
        for line in lines:
            if line.startswith('"'):
                end_index = line.find('"', 1)
                while end_index != -1 and line[end_index-1] == '\\':
                    end_index = line.find('"', end_index + 2)
                if end_index != -1:
                    result.append(line[1:end_index].replace('\"', '"'))
            else:
                result.append(line.split(',')[0])
        return result

if __name__ == '__main__':
    parser = CSVParser()
    sample_csv1 = """column1,column2,column3
"Hello,\"World\",",!
123,456,789"""
    sample_csv2 = """"Python is fun",how are you?
More data,"with \"escaped\" quotes, and",other columns"""
    
    print(parser.parse_csv_first_column(sample_csv1))
    print(parser.parse_csv_first_column(sample_csv2))