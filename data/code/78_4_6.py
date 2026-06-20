class CalendarPath:
    MONTHS = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
               7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    
    @staticmethod
    def month_to_index(month_name):
        for index, name in CalendarPath.MONTHS.items():
            if name == month_name:
                return index
        return None
    
    @staticmethod
    def shortest_path_distance(month1, month2):
        diff = abs(month1 - month2)
        return min(diff, 12 - diff)

if __name__ == '__main__':
    print(CalendarPath.shortest_path_distance(12, 2))