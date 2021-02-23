from abc import ABC, abstractmethod

class ObservableEngine(Engine): # Наблюдаемая система
    def __init__(self): 
        self.__subscribers = set() # При инициализации множество подписчиков задается пустым
    
    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber) # Для того чтобы подписать пользователя, он добавляется во множество подписчиков
        
    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber) # Удаление подписчика из списка
        
    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message) # Отправка уведомления всем подписчикам


class AbstractObserver(ABC):
    @abstractmethod
    def update(self):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, message):
        titles = set([k['title'] for k in self.achievements])
        if message['title'] not in titles:
            self.achievements.append(message)


# shortnot = ShortNotificationPrinter({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})
# fullnot = FullNotificationPrinter({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

# manager = ObservableEngine(Engine)

# manager.subscribe(shortnot)
# manager.subscribe(fullnot)

# manager.notify("Hi!")

# {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}