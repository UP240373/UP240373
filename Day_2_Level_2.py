
# Variables de ejemplo

first_name = str('Abdul')
last_name = str('Mtz Campos')
full_name = str('Abdul Gerardo Mtz Campos')
contry = str('Mexico')
city = str('Aguascalientes')
age = str('18')
year = str('2025')
is_married = bool(True)
is_true = bool(False)
is_light_on = bool(True)
num1, num2, num3, num4, num5 = int(1), int(2), int(3), int(4), int(5)



#       Ejercicios 1

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(contry))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print("")
print("")
print("")



#       Ejercicios 2

print(len(first_name))

print("")
print("")
print("")



#       Ejercicios 3

valor_max = max(len(first_name), len(last_name))
print('el mayor tiene: ', valor_max)

print("")
print("")
print("")



#       Ejercicios 4 a 11

num_one = 5
num_two = 4

variable_total = num_one + num_two
print(num_one, ' + ', num_two, ' = ', variable_total)

variable_diff = num_two - num_one
print(num_two, ' - ', num_one, ' = ', variable_diff)

variable_product = num_two * num_one
print(num_two, ' * ', num_one, ' = ', variable_product)

variable_division = num_one / num_two
print(num_one, ' / ', num_two, ' = ', variable_division)

variable_remainder = num_two % num_one
print(num_two, ' % ', num_one, ' = ', variable_remainder)

variable_exp = num_one ** num_two
print(num_one, ' ** ', num_two, ' = ', variable_exp)

variable_division = num_one // num_two
print(num_one, ' // ', num_two, ' = ', variable_division)

print("")
print("")
print("")



#       Ejercicios 12

radius = 30

area_of_circle = 3.1416 * (radius ** 2)     # 1
print('El area del circulo es: ', area_of_circle)

circum_of_circle = 2 * 3.1416 * radius      # 2
print('La circunferencia del circulo es: ', circum_of_circle)

print("")
print("")
print("")

radius = float(input('Introduce el radio del circulo: '))  #3

area_of_circle = 3.1416 * (radius ** 2)
print('El area de su circulo es: ', area_of_circle)

circum_of_circle = 2 * 3.1416 * radius
print('La circunferencia de su circulo es: ', circum_of_circle)

print("")
print("")
print("")



#       Ejercicios 13

first_name = input('Introduce tu primer nombre = ')
last_name = input('Introduce tus apellidos = ')
contry = input('Introduce tu pais de nacimiento = ')
age = input('Introduce tu edad = ')

print("")
print("")
print("")

print(first_name)
print(last_name)
print(contry)
print(age)

print("")
print("")
print("")








