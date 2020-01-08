import pygame



def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Для того, чтобы перейти в Правила игры, нажмите S",
                  ""
                  "Для того, чтобы приступить к игре, нажмите B"
                  ""
                  "Для того, чтобы изменить уровень, нажмите A"
                  ]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
            elif event.type == pygame.K_s:
                print('Игрок управляет длинным, тонким существом, напоминающим змею, которое ползает по плоскости '
                      '(как правило, ограниченной стенками), собирая еду (или другие предметы), избегая столкновения '
                      'с собственным хвостом и краями игрового поля. В некоторых вариантах на поле присутствуют '
                      'дополнительные препятствия. Каждый раз, когда змея съедает кусок пищи, она становится длиннее, '
                      'что постепенно усложняет игру. Игрок управляет направлением движения головы змеи (обычно 4 направления: вверх, вниз, влево, вправо), '
                      'а хвост змеи движется следом. Игрок не может остановить движение змеи.')

def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))



clock = pygame.time.Clock()



# основной персонаж
player = None

# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level1(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '@':
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y





class Snake(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 15, tile_height * pos_y + 5)
        self.pos = (pos_x, pos_y)

    def move(self, x, y):
        self.pos = (x, y)
        if event.key == pygame.K_UP:
            while self.pos != ( x, 0):
                self.rect = self.image.get_rect().move(title_width * self.pos[0], title_height * self.pos[1] + 50)
        elif event.key == pygame.K_DOWN:
            while self.pos != (x, 1200):
                self.rect = self.image.get_rect().move(title_width * self.pos[0], title_height * self.pos[1] - 50)
        elif event.key == pygame.K_LEFT:
            while self.pos != (0, y):
                self.rect = self.image.get_rect().move(title_width * self.pos[0] - 50, title_height * self.pos[1])
        elif event.key == pygame.K_RIGHT:
            while self.pos != (1200, y):
                self.rect = self.image.get_rect().move(title_width * self.pos[0] + 50, title_height * self.pos[1])



class Balls(Snake):
    def __init__(self):
        super().__init__()
        self.rad = 10
        self.count = 0

    def draw_apples(self):
        image = load_image("apples.png")



def create_block():
    """ Создает блок в случайной позиции на карте """
    global BLOCK
    posx = SEG_SIZE * (random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE))
    posy = SEG_SIZE * (random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE))

    # блок это кружочек красного цвета
    BLOCK = c.create_oval(posx, posy,
                          posx + SEG_SIZE,
                          posy + SEG_SIZE,
                          fill="red")


pygame.init()

size = width, height = 1200, 1200
screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()