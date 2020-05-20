"""
    CopyRight Dr. Ahmad Hamdi Emara 2020
    Adam Medical Company
"""

import sys
from dataclasses import dataclass
def main():
    Salary(Config()).calculate()

@dataclass
class Config:
    def __init__(self):
        self.sep =  '=-=' * 20
        self.default_list_factor = 7.19
        self.default_list = 1907.64
        self.default_overtime = 38.9
        self.default_sales = 219000.0/2.0
        self.default_bonus = 700.0
        self.base_salary = 4500.0
        self.default_discount = 0.0
        self.single_housing_allowance = round(15000.0 / 12.0, 2)
        self.married_housing_allowance = round(17000.0 / 12.0, 2)

class Formatter:
    def __init__(self, config, args_availble):
        self.config = config
        self.args_availble = args_availble
        
    def print_defaults(self):
        print(self.config.sep)
        print(f"Base salary: {self.config.base_salary}")
        print(f"Single housing allowance:  {self.config.single_housing_allowance}")
        print(f"Married housing allowance: {self.config.married_housing_allowance}")
        print(f"Overtime hours: {self.config.default_overtime}")
        print(f"This month bonuses: {self.config.default_bonus}")
        print(self.config.sep)

class Salary:
    def __init__(self, config):
        self.config = config
        self.formatter = Formatter(config, False)
        

    def calculate(self):
        self.formatter.print_defaults()
        lst = self.config.default_list
        sold_list = round((100.0 * lst) / self.config.default_list_factor, 2)
        total_sales = self.config.default_sales - sold_list
        kpi = round((sold_list / self.config.default_sales)*100,2)
        
        print(f"Total sales without the list items: {total_sales}" )
        print(self.config.sep)

        print(f'Your KPI This month is {kpi} %')
        print(self.config.sep)

        cut = round(total_sales * 0.01, 2)
        print(f"Sales cut: {cut}")
        print(self.config.sep)

        discounted = self.config.default_discount

        overtime_hr_value = round((self.config.base_salary / 26.0 / 10.0) * 1.5, 2)
        total_overtime = round(self.config.default_overtime * overtime_hr_value, 2)
        print(f"Total overtime value: {total_overtime}")
       

        total_salary_without_allowance = round(self.config.base_salary - discounted + total_overtime + lst + cut + self.config.default_bonus, 2)
        total_married_salary = round(total_salary_without_allowance + self.config.married_housing_allowance, 2)
        total_single_salary = round(total_salary_without_allowance + self.config.single_housing_allowance, 2)
        
        print(self.config.sep)
        print(f"Married salary: {total_married_salary}")
        print(self.config.sep)

        print(f"Single salary: {total_single_salary}" )
        print(self.config.sep)

if __name__ == "__main__":
    main()
