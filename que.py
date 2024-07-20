from collections import deque


class FoodQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, order):
        self.queue.append(order)
        print(f"เพิ่มออร์เดอร์: {order}")

    def dequeue(self):
        if not self.is_empty():
            order = self.queue.popleft()
            print(f"ลูกค้ารับออร์เดอร์: {order}")
        else:
            print("ไม่มีออร์เดอร์ในคิว")

    def is_empty(self):  # ตรวจสอบว่าคิวว่างหรือไม่
        return len(self.queue) == 0

    def display_queue(
        self,
    ):  # display_queue จะพิมพ์รายการอาหารที่อยู่ในคิวทั้งหมด โดยจะแสดงทีละรายการ.
        print("ออร์เดอร์ที่รอในคิว")
        if not self.is_empty():
            for order in self.queue:
                print(order)


# สร้างคิวรับอาหารของภัตตาคราร
food_queue = FoodQueue()

while True:
    print("\nกรุณาเลือกรายการอาหาร")
    print("1. เพิ่มออร์เดอร์")
    print("2. รับออร์เดอร์แรก")
    print("3. แสดงรายการอาหารออร์เดอร์ในคิว")
    print("4. ออกจากโปรแกรม")

    choice = input("กรุณาเลือกทำรายการ :")

    if choice == "1":
        order = input("กรุณาใส่ชื่อออร์เดอร์: ")
        food_queue.enqueue(order)
    elif choice == "2":
        food_queue.dequeue()

    elif choice == "3":
        food_queue.display_queue()

    elif choice == "4":
        print("ออกจากโปรแกรม")
        break

    else:
        print("กรุณาเลือกรายการใหม่อีกครั้ง: ")
