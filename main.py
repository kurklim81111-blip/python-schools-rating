# ООП
import json

class Building:
    def __init__(self, year, city):
        self.year = year
        self.city = city
    
class School(Building):
    def __init__(self, year, city, students):
        super().__init__(year, city)
        self.students = students

class Class_students(School):
    def __init__(self, year, city, students, students_class):
        super().__init__(year, city, students)
        self.students_class = students_class  

# Допустим, задача сравнить кол-во учеников в выбранном классе в разных школах
# Загрузка данных из файла .json

with open("schools.json", "r", encoding="utf8") as file:
    data = json.load(file)
    spisok_school = []
    for element in data:
        try:
            year = element["year"]
            city = element["city"]
            students = element["students"]
            students_class = element["students_class"]
        except KeyError:
            print("Данных о школе нет")
            continue
        
        school_info = Class_students(year, city, students, students_class)
        spisok_school.append(school_info)

rating = sorted(spisok_school, key=lambda school: school.students_class, reverse=True)

# Отчёт
print("="*75)
print("Рейтинг школ по количеству учеников в классе")
print("="*75)

for index, school in enumerate(rating, start = 1):
    print("-"*150)
    print(f"{index} место: школа города {school.city} - {school.students_class} учеников в классе. Всего учеников в школе: {school.students}, а построена школа была в {school.year} году.")
    print("-"*150)
    
print("="*75)

# Открываем файл для записи
with open("rating.txt", "w", encoding="utf8") as report_file:
    report_file.write("="*75 + "\n")
    report_file.write("РЕЙТИНГ ШКОЛ ПО КОЛИЧЕСТВУ УЧЕНИКОВ В 11 КЛАССЕ\n")
    report_file.write("="*75 + "\n\n")
    
    for index, school in enumerate(rating, start=1):
        line = (f"{index} место: {school.city} | "
                f"Учеников в классе: {school.students_class} | "
                f"Всего в школе: {school.students} | "
                f"Год постройки: {school.year}\n")
        
        report_file.write(line)

print("\nОтчет успешно сохранен в файл rating.txt\n")