import flet as ft


def main(page: ft.Page):
    page.title = "Ping Pong"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.GREEN_ACCENT_400)
    page.update()

    page.add(
        ft.Row(
            [
                ft.Container(
                    alignment=ft.alignment.top_left,
                    margin=1,
                    padding=4,
                    width=980,
                    height=42,
                    #bgcolor=ft.Colors.INDIGO,
                    border_radius=ft.border_radius.all(2),
                    content=ft.Row([   
                        ft.ElevatedButton(
                            adaptive=True,
                            bgcolor={"pressed": ft.Colors.TEAL_ACCENT_200, "default": ft.Colors.GREEN},
                            color="black",
                            content=ft.Row([
                                
                                ft.Image(src="Flet/ping.png", width=35, height=35),
                                ft.Text("Start ALL PING", size=24),
                                ft.Image(src="Flet/ping.png", width=35, height=35),

                                
                            ],
                                tight=True,
                            ),
                            on_click=lambda e:print("Pressionado start all ping"),
                        ),
                        ft.ElevatedButton(
                            adaptive=True,
                            bgcolor={"pressed": ft.Colors.RED_100, "default": ft.Colors.RED},
                            color="write",
                            content=ft.Row([
                                
                                ft.Image(src="Flet/stop.png", width=35, height=35),
                                ft.Text("Stop ALL PING", size=24),
                                ft.Image(src="Flet/stop.png", width=35, height=35),
                                
                            ],
                                tight=True,
                            ),
                        ),
                        ft.ElevatedButton(
                            adaptive=True,
                            bgcolor={"pressed":ft.Colors.AMBER_200, "default":ft.Colors.ORANGE},
                            color="black",
                            content=ft.Row([
                                
                                ft.Image(src="Flet/insert.png", width=30, height=30),
                                ft.Text("Insert New IP", size=24),
                                ft.Image(src="Flet/insert.png", width=30, height=30),
                                
                            ],
                                tight=True,
                            ),
                        ),
                    ],
                    alignment="end"
                    ),
                    
                    
                ),
                ft.Container(
                    alignment=ft.alignment.top_right,
                    margin=1,
                    padding=8,
                    width=270,
                    height=42,
                    #bgcolor=ft.Colors.INDIGO,
                    border_radius=ft.border_radius.all(2),  
                    content=ft.Row(
                                [
                                    ft.Image(src="Flet/ip.png", width=35, height=35),
                                    ft.Text("My IP: ", size=20, color="write"),
                                    ft.Text("0.0.0.0", size=20, color="write"),
                                ],
                            ),
                   
                ),
            ],
            alignment="center",
        ),
    )
    page.update()

ft.app(target=main)
