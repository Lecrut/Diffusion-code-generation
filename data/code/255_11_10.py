class FileReader:
    MAX_VAL_ERROR = "Unable to find maximum value in file: "

    @staticmethod
    def read_and_find_max(file_path):
        try:
            with open(file_path, 'r') as file:
                data = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
                if not data:
                    raise ValueError("No numeric data found in the file")
                return max(data)
        except FileNotFoundError:
            print(FileReader.MAX_VAL_ERROR + "File not found.")
        except ValueError as e:
            print(FileReader.MAX_VAL_ERROR + str(e))
        return None

if __name__ == '__main__':
    result1 = FileReader.read_and_find_max('sample.txt')
    print(result1)

    result2 = FileReader.read_and_find_max('empty.txt')
    print(result2)

    result3 = FileReader.read_and_find_max('non_numeric.txt')
    print(result3)