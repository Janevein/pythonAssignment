# def factorial (x): # Factorial problem
#     if x == 0:
#         return 1
#     return x * factorial(x-1)
# print (factorial(5))

#sumofdigits
# def SumofDigits(num):
#     if num < 0:
#         num = num * -1
#         return SumofDigits(num)
#     if num < 10:
#         return num
#     return (num % 10) + SumofDigits(num // 10) # Modulus (%) represents the last num becuz it return the remainder and // represent the answer of divison with no decimal
# print(SumofDigits(2345))

# my_dict = {}
# i = 0
# def twoSum (nums, target):
#  for i in range (len(nums)):
#     if str(target - nums[i])  in my_dict:
#         return (i, my_dict[str(target -nums[i])])
#     my_dict [str(nums[i])] = i
# print(twoSum([5,5,6], 10))

#reverse string
def reverse (str):
    strx = str [6:]
    str = str.strip()
    return str
print (reverse ("Khaing Thazin Phyoe"))



