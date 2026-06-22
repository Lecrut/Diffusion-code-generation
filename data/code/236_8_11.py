class PatternRepeater:
    BASE_PATTERN = "O"
    
    @staticmethod
    def repeat_pattern(multiplier: int) -> str:
        return PatternRepeater.BASE_PATTERN * multiplier
    
if __name__ == '__main__':
    result = PatternRepeater.repeat_pattern(20)
    print(result)