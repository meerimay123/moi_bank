def calculate_min_number(numbers: list) -> int:
    """Возвращает минимальное число в списке"""
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number

    return  min_number

def calculate_max_number(numbers: list) -> int:
    """Возвращает максимальное число в списке"""
    max_number = numbers[0]
    for number in numbers:
        if number < max_number:
            max_number = number

    return max_number

class Structure:

    def __init__(self, numbers_pm: list):
        self.numbers = numbers_pm

    def caculate_min_number(self):
        """Возвращает минимальное число"""
        min_number = self.numbers[0]
        for number in self.numbers:
            if number > min_number:
                min_number = number

        return min_number

