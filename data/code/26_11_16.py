import calendar

class VotingEligibilityManager:
    def __init__(self, minimum_age: int = 18, maximum_age: int = 120):
        if not (0 < minimum_age < maximum_age):
            raise ValueError("Invalid age range")
        self.minimum_age = minimum_age
        self.maximum_age = maximum_age

    def calculate_age(self, birth_year: int, birth_month: int, birth_day: int, reference_year: int, reference_month: int, reference_day: int) -> int:
        age = reference_year - birth_year
        if (reference_month, reference_day) < (birth_month, birth_day):
            age -= 1
        if age < 0:
            return 0
        return age

    def is_date_valid(self, year: int, month: int, day: int) -> bool:
        if year < 1:
            return False
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        try:
            max_days = calendar.monthrange(year, month)[1]
            return day <= max_days
        except ValueError:
            return False

    def check_eligibility(self, birth_year: int, birth_month: int, birth_day: int, reference_year: int = 2023, reference_month: int = 11, reference_day: int = 14) -> bool:
        if not self.is_date_valid(birth_year, birth_month, birth_day):
            return False
        if not self.is_date_valid(reference_year, reference_month, reference_day):
            return False
        
        age = self.calculate_age(birth_year, birth_month, birth_day, reference_year, reference_month, reference_day)
        
        if age < self.minimum_age or age > self.maximum_age:
            return False
        
        return age >= self.minimum_age

    def get_eligibility_status(self, birth_year: int, birth_month: int, birth_day: int, reference_year: int = 2023, reference_month: int = 11, reference_day: int = 14) -> dict:
        valid_date = self.is_date_valid(birth_year, birth_month, birth_day)
        age = 0
        eligible = False
        
        if valid_date:
            age = self.calculate_age(birth_year, birth_month, birth_day, reference_year, reference_month, reference_day)
            eligible = self.check_eligibility(birth_year, birth_month, birth_day, reference_year, reference_month, reference_day)
        
        return {
            "age": age,
            "eligible": eligible,
            "valid_date": valid_date
        }

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    
    result1 = manager.get_eligibility_status(2000, 1, 1)
    print(result1)
    
    result2 = manager.check_eligibility(2010, 1, 1)
    print(result2)