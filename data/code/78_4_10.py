class CalendarDistance:
    def __init__(self):
        self.months = ["January", "February", "March", "April", "May", "June", 
                       "July", "August", "September", "October", "November", "December"]
    
    def month_to_index(self, month_name):
        return self.months.index(month_name) + 1
    
    def shortest_path_distance(self, month1, month2):
        index1 = self.month_to_index(month1)
        index2 = self.month_to_index(month2)
        return min(abs(index1 - index2), 12 - abs(index1 - index2))

if __name__ == '__main__':
    calendar = CalendarDistance()
    print(calendar.shortest_path_distance("December", "February"))