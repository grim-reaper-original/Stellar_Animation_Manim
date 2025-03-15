%%manim -qm -v WARNING StarLifeIntro



class StarLifeIntro(Scene):
    def construct(self):
        # Title Text
        title = Text("The Life Cycle of a Star", font_size=48)
        self.play(Write(title))
        self.wait(1)

        # Fade Out Title
        self.play(FadeOut(title))

        star_colors = [WHITE, BLUE, YELLOW, RED]
        num_stars = 500
        # Background - Simulated Starfield or Nebula
        stars = VGroup(*[Dot(
                point=[np.random.uniform(-4, 4), np.random.uniform(-2.5, 2.5), 0],  # Spread stars more evenly
                radius=np.random.uniform(0.01, 0.03),  # Vary star sizes
                color=np.random.choice(star_colors)  # Randomize colors
            )
            for _ in range(num_stars)
        ])



        # Introduction Text
        intro_text = Text(
            "Stars are born from clouds of gas and dust,\n"
            "live for millions to billions of years,\n"
            "and die in spectacular ways.",
            font_size=32
        )

        self.play(FadeIn(stars))
        self.wait(1)
        self.play(Write(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))

        target_star = next(star for star in stars if star.get_color() == YELLOW)

        self.play(*[star.animate.fade(1) for star in stars if star != target_star])
        self.wait(1)

        # Highlight the target star by increasing its size
        self.play(target_star.animate.scale(50))
        self.wait(1)

        self.play(target_star.animate.move_to(ORIGIN))
        self.wait(1)

        # Create the explanation text
        star_life_text = Text(
    "We shall study this little yellow guy here,\n"
    "and see how he lives his entire life",
        font_size=28).next_to(target_star, UP)
        self.play(Write(star_life_text))

        self.play(FadeOut(target_star, star_life_text))

        intro_text = Text(
            "It all starts with clumps of dust and gases floating through space.",
            font_size=28
        )
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Create nebula particles
        nebula_particles = VGroup(*[
            Dot(
                point=[np.random.uniform(-3, 3), np.random.uniform(-2, 2), 0],
                radius=0.02,  # Uniform size
                color=MAROON   # Brown dust particles
            )
            for _ in range(100)  # Number of dust particles
        ])

        # Show the nebula
        self.play(FadeIn(nebula_particles))
        self.wait(1)

        # Explanation before nebula contracts
        collapse_text = Text(
            "Usually, enough dust appears in one place,\n"
            "such that the combined mass causes gravitational attraction,\n"
            "causing the dust to gather into a single mass entity.",
            font_size=24
        ).to_edge(UP)

        self.play(Write(collapse_text))
        self.wait(1)

        # # Animate contraction towards center
        # self.play(nebula_particles.animate.scale(0.5).move_to(ORIGIN), run_time=3)
        # self.wait(1)

        self.play(FadeOut(collapse_text))

        # Transform into a protostar (brown-yellow color)
        protostar = Dot(ORIGIN, radius=0.3, color=rgb_to_color((0.8, 0.6, 0.2)))  # Brown-Yellow
        new_text = MathTex(r"\leftarrow \text{ Protostar}", font_size=36)
        new_text.next_to(protostar, RIGHT)

        self.play(Transform(nebula_particles, protostar))
        self.wait(1)

        self.play(Write(new_text))
        self.wait(1)
        self.play(FadeOut(protostar,new_text))
%%manim -qm -v WARNING StarLifeIntro

class StarLifeIntro(Scene):
    def construct(self):
        # New explanation text for fusion initiation
        fusion_text = Text(
            "Now the temperature in the center is sooo high\n"
            "that hydrogen overcomes repulsion forces\n"
            "and fuses to form helium!",
            font_size=28
        )

        self.play(FadeIn(fusion_text))
        self.wait(2)
        self.play(FadeOut(fusion_text))

        fusion_text1 = Text(
            "This gives out largee amount of energy\n"
            "and this is when we call it a main sequence star\n",
            font_size=28
        )

        self.play(FadeIn(fusion_text1))
        self.wait(2)
        self.play(FadeOut(fusion_text1))

        # New explanation text for fusion initiation
        fusion_text = Text(
            "Now the temperature in the center is sooo high\n"
            "that hydrogen overcomes repulsion forces\n"
            "and fuses to form helium!",
            font_size=28
        )

        self.play(FadeIn(fusion_text))
        self.wait(2)
        self.play(FadeOut(fusion_text))

        fusion_text1 = Text(
            "This gives out largee amount of energy\n"
            "and this is when we call it a main sequence star\n",
            font_size=28
        )

        self.play(FadeIn(fusion_text1))
        self.wait(2)
        self.play(FadeOut(fusion_text1))

        # Create a bigger yellow dot representing the star
        main_star = Dot(ORIGIN, radius=3, color=YELLOW)

        # Define arrow properties
        arrow_length = 1
        arrow_thickness = 0.07

        # Outward arrows (Gas Pressure)
        gas_pressure_arrows = VGroup(
            Arrow(RIGHT * 3, RIGHT * (3 + arrow_length), buff=0, color=RED, stroke_width=8),
            Arrow(LEFT * 3, LEFT * (3 + arrow_length), buff=0, color=RED, stroke_width=8),
            Arrow(UP * 3, UP * (3 + arrow_length), buff=0, color=RED, stroke_width=8),
            Arrow(DOWN * 3, DOWN * (3 + arrow_length), buff=0, color=RED, stroke_width=8)
        )

        # Labels for gas pressure
        gas_labels = VGroup(
            Text("Gas Pressure", font_size=24, color=RED).next_to(gas_pressure_arrows[0], RIGHT)
        )

        # Inward arrows (Gravity)
        gravity_arrows = VGroup(
            Arrow(RIGHT * (3 + arrow_length), RIGHT * 3, buff=0, color=GRAY, stroke_width=8),
            Arrow(LEFT * (3 + arrow_length), LEFT * 3, buff=0, color=GRAY, stroke_width=8),
            Arrow(UP * (3 + arrow_length), UP * 3, buff=0, color=GRAY, stroke_width=8),
            Arrow(DOWN * (3 + arrow_length), DOWN * 3, buff=0, color=GRAY, stroke_width=8)
        )


        # Labels for gravity
        gravity_labels = VGroup(
            Text("Gravity", font_size=24, color=GRAY).next_to(gravity_arrows[0], LEFT),
        )

        # Animate the appearance of the elements
        self.play(FadeIn(main_star))
        self.play(
            LaggedStart(*[GrowArrow(arrow) for arrow in gas_pressure_arrows], lag_ratio=0.2),
            LaggedStart(*[GrowArrow(arrow) for arrow in gravity_arrows], lag_ratio=0.2)
        )
        self.play(Write(gas_labels), Write(gravity_labels))
        self.wait(2)

        # Fade out all elements
        self.play(FadeOut(main_star, gas_pressure_arrows, gravity_arrows, gas_labels, gravity_labels))

        fusion_text2 = Text(
            "This is the stage our star is in.At some point\n"
            "the star will run out of hydrogen and looses its\n"
            "fuel so,no more nuclear fusion occours\n",
            font_size=28
        )
        self.play(FadeIn(fusion_text2))
        self.wait(2)
        self.play(FadeOut(fusion_text2,))


        fusion_text2 = Text(
            "The inward force of gravity dominates.And the star\n"
            "shrinks,this increases the temperature and\n"
            "nuclear fusion to the next element stars again\n",

            font_size=28
        )
        self.play(FadeIn(fusion_text2))
        self.wait(2)
        self.play(FadeOut(fusion_text2))


        # Animate the star shrinking
        shrinking_star = Dot(ORIGIN, radius=2, color=YELLOW)

        # Animate shrink and remove gas pressure arrows
        self.play(Transform(main_star, shrinking_star))
        self.wait(1)

        # Keep only gravity arrows visible
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in gravity_arrows], lag_ratio=0.2))
        self.play(Write(gravity_labels))
        self.wait(2)

        # Optional: Fade everything out after
        self.play(FadeOut(shrinking_star, gravity_arrows, gravity_labels))



        # Create the text for heavier element formation
        element_text = Text(
            "Now heavier elements are formed up to iron", font_size=28
        ).to_edge(UP)

        # Display the text
        self.play(Write(element_text))
        self.wait(2)
        self.play(FadeOut(element_text, shrinking_star))

        # Animate the star shrinking
        shrinking_star = Dot(ORIGIN, radius=2, color=YELLOW)

        # Animate shrink and remove gas pressure arrows
        self.play(Transform(main_star, shrinking_star))
        self.play(FadeOut(shrinking_star,main_star))


        fusion_text3 = Text(
            "The next stage depends on the size of the star\n",
            font_size=28
        )
        self.play(FadeIn(fusion_text3))
        self.wait(2)
        self.play(FadeOut(fusion_text3))
%%manim -qm -v WARNING StarLifeIntro

class StarLifeIntro(Scene):
    def construct(self):
        # Text and arrow for small/medium stars
        small_medium_text = Text("If it is small or medium", font_size=28).to_edge(LEFT)
        small_medium_arrow = Arrow(LEFT, RIGHT, buff=0.2, color=WHITE).next_to(small_medium_text, RIGHT)

        # Red Giant (edge aligned with arrow tip)
        red_giant_radius = 1.8
        red_giant = Dot(small_medium_arrow.get_end() + RIGHT * red_giant_radius, radius=red_giant_radius, color=RED)
        red_giant_label = Text("Red Giant", font_size=24, color=WHITE).move_to(red_giant)

        # Show text, arrow, and Red Giant
        self.play(Write(small_medium_text), GrowArrow(small_medium_arrow))
        self.play(FadeIn(red_giant), Write(red_giant_label))
        self.wait(2)

        # Make Red Giant disappear
        self.play(FadeOut(red_giant, red_giant_label, small_medium_text, small_medium_arrow))
        self.wait(1)

        # Text and arrow for large stars
        large_text = Text("If it is large", font_size=28).to_edge(LEFT)
        large_arrow = Arrow(LEFT, RIGHT, buff=0.2, color=WHITE).next_to(large_text, RIGHT)

        # Red Supergiant (edge aligned with arrow tip)
        red_supergiant_radius = 2.5
        red_supergiant = Dot(large_arrow.get_end() + RIGHT * red_supergiant_radius, radius=red_supergiant_radius, color=RED)
        red_supergiant_label = Text("Red Supergiant", font_size=24, color=WHITE).move_to(red_supergiant)

        # Show text, arrow, and Red Supergiant
        self.play(Write(large_text), GrowArrow(large_arrow))
        self.play(FadeIn(red_supergiant), Write(red_supergiant_label))
        self.wait(2)
        self.play(FadeOut(large_text,large_arrow,red_supergiant,red_supergiant_label))

        # Explanation text for the White Dwarf formation
        white_dwarf_text = Text(
            "The Red Giant slowly sheds off its outer layers.\n"
            "What remains inside is called a White Dwarf.\n"
            "It gives off a lot of light, so it appears white,\n"
            "and it's called a dwarf because it is small.\n"
            "This does not undergo any further nuclear reactions.",
            font_size=24
        ).to_edge(UP)

        # Show the Red Giant again
        self.play(FadeIn(red_giant), Write(white_dwarf_text))
        self.wait(2)

        # White Dwarf inside the Red Giant
        white_dwarf = Dot(red_giant.get_center(), radius=0.5, color=WHITE)

        # Animate Red Giant fading while revealing White Dwarf
        self.play(red_giant.animate.set_opacity(0.2))  # Fade Red Giant
        self.play(FadeIn(white_dwarf))  # White Dwarf appears
        self.wait(2)

        # Remove text for a clean transition
        self.play(FadeOut(white_dwarf_text,white_dwarf))
        elf.play(red_giant.animate.set_opacity(0))
%%manim -qm -v WARNING Supernova

class Supernova(Scene):
    def construct(self):

        # Supernova explanation text
        supernova_text = Text(
            "Super Red Giants go through reactions more quickly,\n"
            "eventually exploding into a Supernova.\n"
            "This explosion forms even heavier elements\n"
            "that are ejected across the universe.",
            font_size=24
        ).to_edge(UP)

        # Create Red Supergiant
        red_supergiant = Dot(ORIGIN, radius=2.5, color=RED)

        # Background stars
        star_colors = [WHITE, BLUE, YELLOW]
        num_stars = 100
        stars = VGroup(*[
            Dot(
                point=[np.random.uniform(-5, 5), np.random.uniform(-3, 3), 0],
                radius=np.random.uniform(0.01, 0.05),
                color=np.random.choice(star_colors)
            ) for _ in range(num_stars)
        ])

        # Show the background stars
        self.play(FadeIn(stars), run_time=2)

        # Show the Super Red Giant and explanation text
        self.play(FadeIn(red_supergiant), Write(supernova_text))
        self.wait(2)

        # Animate the expansion of the Red Supergiant
        self.play(red_supergiant.animate.scale(1.5), run_time=2)


        # Flash white to simulate explosion
        white_flash = FullScreenRectangle(color=WHITE, fill_opacity=1)
        self.play(FadeIn(white_flash))
        self.wait(0.5)

        # Make background stars disappear
        self.play(FadeOut(white_flash), FadeOut(red_supergiant), FadeOut(stars))

        # Create dust particles spreading out
        dust_particles = VGroup(*[
            Dot(
                point=[np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5), 0],
                radius=np.random.uniform(0.02, 0.08),
                color=rgb_to_color((np.random.uniform(0.5, 1), np.random.uniform(0, 0.5), np.random.uniform(0, 0.5)))
            ).shift(np.random.uniform(0, 2) * RIGHT + np.random.uniform(0, 2) * UP)
            for _ in range(80)
        ])

        # Animate dust particles spreading out
        self.play(FadeIn(dust_particles, shift=OUT), run_time=2)
        self.wait(1)

        # Remove text for a clean transition
        self.play(FadeOut(supernova_text))

        # Display White Dwarf Formation text
        white_dwarf_text = Text(
            "Depending on the size of the supergiant,\n"
            "it can either end up as a white dwarf.",
            font_size=24
        ).to_edge(UP)

        self.play(Write(white_dwarf_text))
        self.wait(1)

        # Create a pulsating white dwarf in the supernova remnant
        white_dwarf = Dot(ORIGIN, radius=0.3, color=WHITE)

        self.play(FadeIn(white_dwarf))
        self.play(white_dwarf.animate.scale(1.2), run_time=1, rate_func=there_and_back)
        self.play(white_dwarf.animate.scale(1.2), run_time=1, rate_func=there_and_back)
        self.play(white_dwarf.animate.scale(1.2), run_time=1, rate_func=there_and_back)

        self.wait(2)

        # Clear the screen
        self.play(FadeOut(white_dwarf), FadeOut(dust_particles), FadeOut(white_dwarf_text))

        # Display Black Hole Formation text
        black_hole_text = Text(
            "If it is massive, it can collapse on itself\n"
            "and form a Black Hole.",
            font_size=24
        ).to_edge(UP)

        self.play(Write(black_hole_text))
        self.wait(2)

        # Animate black hole formation
        black_hole = Dot(ORIGIN, radius=0.1, color=BLACK).set_stroke(WHITE, width=3)

        # Surrounding dust particles spiraling inward
        swirling_particles = VGroup(*[
            Dot(
                point=[np.random.uniform(-2, 2), np.random.uniform(-2, 2), 0],
                radius=np.random.uniform(0.02, 0.05),
                color=rgb_to_color((np.random.uniform(0.2, 1), np.random.uniform(0, 0.5), np.random.uniform(0, 0.5)))
            ) for _ in range(60)
        ])

        self.play(FadeIn(swirling_particles))
        self.play(FadeIn(black_hole))

        # Animate the particles swirling inward
        for _ in range(3):
            self.play(
                swirling_particles.animate.scale(0.7).move_to(ORIGIN),
                run_time=1.5
            )

        # Make everything fade out into darkness
        self.play(FadeOut(swirling_particles, black_hole, black_hole_text), run_time=2)