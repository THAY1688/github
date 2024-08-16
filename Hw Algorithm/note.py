# 1.
# text = input("Enter num!")
# for char in text:
#     print(char)


# 2.
# text = input("Enter num!")
# for i in range(len(text)):
#     print(i)



# 3.
# text = input("Enter your text: ")
# result  = "no"
# for i in range(len(text)):
#     if text[i].upper() == text[i]:
#         result = "Yes"
# print(result)



# 4.
# integer = [3 4 5 6]
# result = 0
# for i in range(len(integer)):
#     result += integer[i]
# print(result)



# 5.1
# integer = "1689025"
# result = 0
# sam = 0
# for i in range(len(integer)):
#     if i % 2 == 0:
#         result += 1
#     elif i % 2 == 1:
#         sam += 1
# print(result)
# print(sam)

# 5.2
# integer = "1689025"
# result = 0
# for i in range(len(integer)):
#     result += int(integer[i])
# print(result)


# 5.3
# integer = "1689025"
# result = 0
# for i in range(len(integer)):
#     if i % 2 == 0:
#         result += 1
#     result += int(integer[i])
# print(result)


# 5.4
# text = input("Enter your text!")
# reversed_text = ""
# for i in range(len(text)):
#     reversed_text += text[len(text) - 1 - i]
# print(reversed_text)


# 6.
# number = int(input("enter a number!"))
# if number % 2 == 1:
#     print("Odd_number")
# else:
#     print("Even_number")



# 7.
# number = int(input("enters a num: "))
# result = "Out of range"
# for u in range(number):
#     if number >= 10 and number <= 20:
#         result = "Continue"
# print(result)



# Ex8 - String
# Q1 - How many number 8 in string
# text = "9394884039"
# Counter_8 = 0
# for char in text:
#     if char == "8":
#         Counter_8 += 1
# print("Counter_8 is: ", Counter_8)


# 9.
# text = "3 4 5 6"
# no_space = ""
# total_x_two = 0
# for i in range(len(text)):
#     if text[i] != " ":
#         no_space += text[i] + " "
#         total_x_two += int(text[i]) * 2
#         print(total_x_two)
#     else:
#         no_space += ""
# print(no_space)

# 10.
# bigest_number = 0
# smailest_number = 0
# for i in range(5):
#     number = int(input("Enter number : "))
#     if bigest_number == 0 and smailest_number == 0:
#         bigest_number = number
#         smailest_number = number
#     else:
#         if number > bigest_number:
#             bigest_number = number
#         if number < smailest_number:
#             smailest_number = number
# print("Bigest number : ", bigest_number)
# print("Smaillest number : ", smailest_number)



