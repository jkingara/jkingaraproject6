import arcade
import random


class Comp151Window(arcade.Window):


    game_window = Comp151Window.Comp151Window(800, 700, "FROGGER GAME")
    game_window.background_color = arcade.color.GREY
    game_window.spider = arcade.Sprite("spider.png")
    game_window.spider.center_y = 100
    game_window.spider.center_x = 600
    game_window.player = arcade.Sprite("Walking turtle 1.png")
    game_window.player.center_x = 400
    game_window.player.center_y = 350
    game_window.mushroom_list = []
    game_window.display_text = "CAN YOU GET TO THE OTHER SIDE?"

    game_window.on_draw = types.MethodType(comp151_draw, game_window)
    game_window.on_key_press = types.MethodType(handle_key_press, game_window)
        arcade.run()

    self.lanes.append(Lane(1, c=(75, 200, 120)))
    self.lanes.append(Lane(2, t='road', (150, 200, 240)))
    self.lanes.append(Lane(3, t='log', (150, 200, 240)))
    self.lanes.append(Lane(4, t='log', (150, 200, 240)))
    self.lanes.append(Lane(5, t='log', (150, 200, 240)))
    self.lanes.append(Lane(6, (75, 200, 120)))
    self.lanes.append(Lane(7, (75, 200, 120)))
    self.lanes.append(Lane(8, t='car', (190, 190, 190)))
    self.lanes.append(Lane(9, t='river', (200, 200, 200)))
    self.lanes.append(Lane(10, t='tank', (190, 190, 190)))
    self.lanes.append(Lane(11, t='car', (200, 200, 200)))
    self.lanes.append(Lane(12, (75, 200, 120)))

    game_window = Comp151Window.Comp151Window(800, 700, "FROGGER GAME")
    game_window.background_color = arcade.color.GREY
    game_window.spider = arcade.Sprite("spider.png")
    game_window.spider.center_y = 100
    game_window.spider.center_x = 600
    game_window.player = arcade.Sprite("Walking turtle 1.png")
    game_window.player.center_x = 400
    game_window.player.center_y = 350
    game_window.mushroom_list = []
    game_window.display_text = "CAN YOU GET TO THE OTHER SIDE?"

    game_window.on_draw = types.MethodType(comp151_draw, game_window)
    game_window.on_key_press = types.MethodType(handle_key_press, game_window)
        arcade.run()

    def on_draw(self):
        if self.state == 'START':
            self.draw_text("GO", , , 'center')
            self.draw_text("Press ENTER to start playing.",,, 'center')

        for mushroom_number in range(6):
                current_sprite = arcade.Sprite("mushroom.png")
                current_sprite.center_x = random.randint(0, 600)
                current_sprite.center_y = random.randint(50, 700)
                game_window.mushroom_list.append(current_sprite)
        arcade.start_render()

    def on_mouse_press(self):
        if self.state == 'PLAYING':
            if event.type == KEYDOWN and event.key == K_LEFT:
                self.frog.move(-1,0)
            if event.type == KEYDOWN and event.key == K_DOWN:
                self.frog.move(1,0)
            if event.type == KEYDOWN and event.key == K_UP:
                self.frog.move (0,-1)
            if event.type == KEYDOWN and event.key == K_RIGHT:
                self.frog.move(1, 0)


main()