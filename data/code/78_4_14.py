class CalendarDistance:
    def __init__(self):
        self.month_to_index = {
            "January": 1,
            "February": 2,
            "March": 3,
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12
        }

    def get_month_index(self, month_name):
        return self.month_to_index.get(month_name)

    def shortest_path_distance(self, month1, month2):
        index1 = self.get_month_index(month1)
        index2 = self.get_month_index(month2)
        return min(abs(index1 - index2), 12 - abs(index1 - index2))

if __name__ == '__main__':
    calendar = CalendarDistance()
    print(calendar.shortest_path_distance("December", "February"))