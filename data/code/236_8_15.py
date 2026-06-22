class ShapeRepeater:
    BASE_PATTERN = "O"
    
    @staticmethod
    def repeat_pattern(multiplier: int) -> str:
        if multiplier <= 0:
            return ""
        return (ShapeRepeater.BASE_PATTERN * multiplier).strip()

if __name__ == '__main__':
    result = ShapeRepeater.repeat_pattern(20)
    print(result)