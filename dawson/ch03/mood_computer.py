import random

print("Я ощущаю вашу энергетику. От моего экрана не скрытно ни одно из ваших чувств.")
print("Итак, ваше настроение...")
mood = random.randint(1, 3)
if mood == 1:
    print(\
        """
         ----------
        |          |
        |  0    0  |
        |    <     |
        |  <====>  |
        |          |
         ----------
        """
        )
elif mood == 2:
    print(\
        """
         ----------
         ----------
        |          |
        |  0    0  |
        |    <     |
        |          |
        |  -----   |
         ----------
        """
        )
elif mood == 3:
    print(
        """
         ----------
        |          |
        |  0    0  |
        |    <     |
        |          |
        |   ////   |
         ----------
        """
    )
else:
    print("Не бывает такого настроения! Должно быть, вы совершенно не в себе.")