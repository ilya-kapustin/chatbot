token = '511d9adac9eba73d0a9e98d82cfac56980242a75438e2977e67001a4283d5236703f4924cce2fc3b0a345'
import vk_api
import vk_api.bot_longpoll

group_id = 205441441


class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception as err:
                print(err)

    def on_event(self, event):
        print(event.message.text)


if __name__ == "__main__":
    bot = Bot(group_id, token)
    bot.run()