from datetime import datetime

class DateFormatter:
    def __init__(self, input_file='dates.txt', output_file='formatted_dates.txt'):
        self.input_file = input_file
        self.output_file = output_file

    def read_dates(self):
        with open(self.input_file, 'r') as file:
            return [line.strip() for line in file]

    def format_dates(self, dates):
        formatted_dates = []
        for date_str in dates:
            try:
                date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                formatted_date = date_obj.strftime('%d/%m/%Y')
                formatted_dates.append(formatted_date)
            except ValueError:
                print(f"Invalid date format: {date_str}")
        return formatted_dates

    def write_dates(self, dates):
        with open(self.output_file, 'w') as file:
            for date in dates:
                file.write(date + '\n')

    def process_dates(self):
        dates = self.read_dates()
        formatted_dates = self.format_dates(dates)
        self.write_dates(formatted_dates)

if __name__ == '__main__':
    formatter = DateFormatter()
    formatter.process_dates()