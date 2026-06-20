class ZellersCongruence:
    DAYS_OF_WEEK = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    @staticmethod
    def zellers_congruence(day, month, year):
        if month < 3:
            month += 12
            year -= 1
        K = year % 100
        J = year // 100
        h = (day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
        return ZellersCongruence.DAYS_OF_WEEK[h]
    
    @staticmethod
    def get_day_of_week(year):
        if year < 1900:
            raise ValueError("Year must be 1900 or later.")
        return ZellersCongruence.zellers_congruence(1, 1, year)

if __name__ == '__main__':
    print(ZellersCongruence.get_day_of_week(1900))