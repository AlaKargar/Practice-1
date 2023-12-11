name = input("Enter your name: ")
family = input("Enter your family: ")
age = input("Enter your age: ")
math = float(input("Enter your math mark: "))
eng = float(input("Enter your English mark: "))
per = float(input("Enter your Persian mark: "))
print("Hi! Your name is", name, family, "and you are",
      age, "years old. your avg is", (math+eng+per)/3)
