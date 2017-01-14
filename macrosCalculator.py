'''
Conversion
9 calories/1g fat
4 calories/1g protein
4 calories/1g carb


Macros
fat_range = .20 to .30 
- Ideal is .25 or 25%

grams_protein = 1g protein per lb body weight
grams_fat = total_calories * fat_range / (9 calories/1g fat)
grams_carbs = (total_calories - grams_protein * (4 calories/1g protein) - grams_fat * (9 calories/1g fat)) / (4 calories/1g carb)


Example
total_calories = 2420 calories
body_weight = 135 lb

grams_protein = 135g
grams_fat = 2420 * .25 / 9 = 67.2222g 
grams_carbs = (2420 - (135 * 4) - (67.2222 * 9))/4 = 318.7501g 
'''

total_calories = input('Enter your total daily calories: ')
body_weight = input('Enter your current body weight in lbs: ')
fat_range = input('Enter a fat range from .20 to .30: ')

grams_protein = body_weight
grams_fat = total_calories * fat_range / 9
grams_carbs = (total_calories - (grams_protein * 4) - (grams_fat *9))/4

print "Protein: %dg\nFat: %dg\nCarbs: %dg" % (grams_protein, grams_fat, grams_carbs)

