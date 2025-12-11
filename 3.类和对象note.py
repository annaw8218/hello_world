'''
演示类和对象的关系，即面向对象编程。
类是设计图纸，对象是生产实体。
'''
import pygame
pygame.mixer.init()

# 设计一个闹钟类
class Clock:
    id = None  # 序列号
    price = None  # 价格

    def ring(self):
        pygame.mixer.Sound("beep.wav")  # I can't make it sound correctly

# 构建2个闹钟对象并让其工作
clock1 = Clock()
clock1.id = "3003"
clock1.price = 19.9
print(f'ID:{clock1.id}, price:{clock1.price}')
clock1.ring()

clock2 = Clock()
clock2.id = 3004
clock2.price = 21.1
print(f'ID:{clock2.id}, price:{clock2.price}')
clock2.ring

for i in range(5):
    print("*"*i)
    
