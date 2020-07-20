ALLERGIES = ['eggs', 'peanuts', 'shellfish', 'strawberries',
             'tomatoes', 'chocolate', 'pollen', 'cats']


class Allergies:

    def __init__(self, score):
        self.lst = [item for i, item in enumerate(ALLERGIES) if 1 << i & score]

    def allergic_to(self, item):
        return item in self.lst
