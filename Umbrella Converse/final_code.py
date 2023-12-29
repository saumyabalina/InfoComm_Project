from manim import *

class Introduction(Scene):
    def construct(self):
        umbrella_img = ImageMobject("Final Background")
        umbrella_img.scale(2.7)
        self.play(FadeIn(umbrella_img))
        self.wait(2)
        text = Text("Umbrella Converse", font="Times New Roman", color=WHITE).scale(2)
        text.shift(UP * 3 + LEFT * 1.75)
        self.play(Write(text))
        self.wait(2)
        t1 = Text("Saumya Balina (2022102069)").scale(0.8)
        t2 = Text("Himani Sharma (2022102032)").scale(0.8)
        t2.shift(DOWN*0.75)
        gr = VGroup(t1, t2)
        gr.shift(DOWN * 2.5 + RIGHT * 3.2)
        self.play(FadeIn(gr))
        self.wait(2)
        gr = VGroup(gr, text)
        self.play(
            umbrella_img.animate.shift(LEFT * 50),
            gr.animate.shift(LEFT * 50),
            run_time=3,
        )
        self.remove(umbrella_img, gr)
        self.wait(7)
        text = Text("MODEL", weight=BOLD)
        text.shift(UP * 3 + LEFT * 5)
        self.play(Write(text))
        text1 = Tex(
            "The model of the paper is to study the problem of data exchange in a networked environment. The paper aims to derive lower bounds and converses for various settings and scenarios, with a focus on coded caching, computing, and shuffling using mathematical and information-theoretic techniques."
        ).scale(0.8)
        self.play(Write(text1))
        self.wait(20)
        gr = VGroup(text, text1)
        self.play(FadeOut(gr))

        text = Text("PROBLEM", weight=BOLD)
        text.shift(UP * 3 + LEFT * 5)
        self.play(Write(text))
        text1 = Tex(
            "The problem that the author is trying to solve in this paper is the efficient exchange of data between multiple nodes in a network. The author aims to design communication schemes that minimize the amount of data transmitted while ensuring that each node has access to the desired data. The author's specific goal is to develop a converse to the data exchange problem, which provides an expression that depends only on the number of bits to be moved between different subsets of nodes."
        ).scale(0.8)
        self.play(Write(text1))
        self.wait(27)
        gr = VGroup(text, text1)
        self.play(FadeOut(gr))

class SingleNode(Scene):
    def construct(self):
        blockC = Rectangle(height=2, width=1.9, color=WHITE)
        blockD = Rectangle(height=2, width=1.9, color=WHITE)
        blockC.shift(UP)
        blockD.shift(DOWN)

        text = MathTex(r"{C_i}", font_size=72)
        text.move_to(blockC)
        blockC = VGroup(blockC, text)
        text = MathTex(r"{D_i}", font_size=72)
        text.move_to(blockD)
        blockD = VGroup(blockD, text)

        block = VGroup(blockC, blockD)
        text = Tex("Node", font_size=72)
        text.shift(DOWN, DOWN, 0.5 * DOWN)
        # self.wait(1)
        self.play(FadeIn(block))
        self.play(FadeIn(text))
        self.wait(5)
        self.play(FadeOut(text), run_time=0.5)

        self.play(block.animate.shift(LEFT, LEFT, LEFT, LEFT, LEFT))
        self.wait(1)

        C = blockC.copy()
        D = blockD.copy()
        self.play(
            C.animate.scale(1.25).move_to(RIGHT * 2 + UP * 2.5),
            D.animate.scale(1.25).move_to(RIGHT * 2 + DOWN * 2.5),
        )

        text1 = Text("Local\nStorage")
        text2 = Text("Demanded\nBits")
        text1.next_to(C)
        text2.next_to(D)
        self.play(text1.animate, text2.animate)
        self.wait(20)

class Encode(Scene):
    def construct(self):
        block_red = RoundedRectangle(height=1.5, width=2, color=RED_C)
        block_red.set_fill(color=RED_C, opacity=0.35)
        block_red.shift(LEFT, LEFT, LEFT, LEFT, LEFT)
        block_encoder = Rectangle(color=GREY)
        block_encoder.set_fill(color=GREY, opacity=0.5)
        text = MathTex(r"{C_i}")
        text.scale(0.8)
        text.move_to(block_red)
        block_red = VGroup(block_red, text)
        text = Tex("Encoder", font_size=72)
        text.scale(0.8)
        text.move_to(block_encoder)
        block_encoder = VGroup(block_encoder, text)
        arrow1 = Arrow(block_red.get_right(), block_encoder.get_left())

        text = Tex("Codeword", font_size=64)
        text.shift(RIGHT, RIGHT, RIGHT, RIGHT, RIGHT)
        text2 = MathTex("(Length = {l_i})", font_size=48)
        text2.shift(RIGHT, RIGHT, RIGHT, RIGHT, RIGHT, DOWN)
        arrow2 = Arrow(block_encoder.get_right(), text.get_left())
        tex = MathTex(r"\phi_i : \{0, 1\}^{|C_i|} \rightarrow \{0, 1\}^{l_i}")
        tex.shift(DOWN, DOWN)
        self.play(Create(block_red), run_time=2)
        self.play(Create(arrow1), run_time=2)
        self.play(Create(block_encoder), Create(tex), run_time=2)
        self.play(Create(arrow2))
        self.play(Create(text), Create(text2), run_time=2)
        self.wait(2)

class Illustrate2(Scene):
    def construct(self):
        blockC_red = RoundedRectangle(height=1.5, width=2, color=RED)
        blockC_red.set_fill(color=RED, opacity=0.5)
        blockC_blue = RoundedRectangle(height=1.5, width=2, color=BLUE)
        blockC_blue.set_fill(color=BLUE, opacity=0.5)
        blockC_green = RoundedRectangle(height=1.5, width=2, color=GREEN)
        blockC_green.set_fill(color=GREEN, opacity=0.5)
        blockC_red.shift(LEFT, LEFT, LEFT, LEFT, UP, UP, UP)
        blockC_blue.shift(LEFT, LEFT, LEFT, LEFT)
        blockC_green.shift(LEFT, LEFT, LEFT, LEFT, DOWN, DOWN, DOWN)

        blockD_red = RoundedRectangle(height=1.5, width=2, color=RED)
        blockD_red.set_fill(color=RED, opacity=0.5)
        blockD_blue = RoundedRectangle(height=1.5, width=2, color=BLUE)
        blockD_blue.set_fill(color=BLUE, opacity=0.5)
        blockD_green = RoundedRectangle(height=1.5, width=2, color=GREEN)
        blockD_green.set_fill(color=GREEN, opacity=0.5)
        blockD_red.shift(RIGHT, RIGHT, RIGHT, RIGHT)
        blockD_blue.shift(RIGHT, RIGHT, RIGHT, RIGHT, DOWN, DOWN, DOWN)
        blockD_green.shift(RIGHT, RIGHT, RIGHT, RIGHT, UP, UP, UP)

        text = Text("C1")
        text.scale(0.8)
        text.move_to(blockC_red)
        blockC_red = VGroup(blockC_red, text)

        text = Text("C2")
        text.scale(0.8)
        text.move_to(blockC_blue)
        blockC_blue = VGroup(blockC_blue, text)

        text = Text("C3")
        text.scale(0.8)
        text.move_to(blockC_green)
        blockC_green = VGroup(blockC_green, text)

        text = Text("D2")
        text.scale(0.8)
        text.move_to(blockD_red)
        blockD_red = VGroup(blockD_red, text)

        text = Text("D3")
        text.scale(0.8)
        text.move_to(blockD_blue)
        blockD_blue = VGroup(blockD_blue, text)

        text = Text("D1")
        text.scale(0.8)
        text.move_to(blockD_green)
        blockD_green = VGroup(blockD_green, text)

        grC = VGroup(blockC_red, blockC_blue, blockC_green)
        grD = VGroup(blockD_red, blockD_blue, blockD_green)
        gr = grC + grD
        self.play(gr.animate)
        self.wait(1)

        arrow11 = Arrow(blockC_red.get_right(), blockD_blue.get_left())
        arrow21 = Arrow(blockC_red.get_right(), blockD_green.get_left())
        arrow31 = Arrow(blockC_red.get_right(), blockD_red.get_left())
        self.play(Write(arrow11), Write(arrow21), Write(arrow31))

        self.wait(2)
        self.play(FadeOut(arrow11), FadeOut(arrow21))

        arrow12 = Arrow(blockC_blue.get_right(), blockD_blue.get_left())
        arrow22 = Arrow(blockC_blue.get_right(), blockD_green.get_left())
        arrow32 = Arrow(blockC_blue.get_right(), blockD_red.get_left())
        self.play(Write(arrow12), Write(arrow22), Write(arrow32))
        self.wait(2)
        self.play(FadeOut(arrow22), FadeOut(arrow32))

        arrow13 = Arrow(blockC_green.get_right(), blockD_blue.get_left())
        arrow23 = Arrow(blockC_green.get_right(), blockD_green.get_left())
        arrow33 = Arrow(blockC_green.get_right(), blockD_red.get_left())
        self.play(Write(arrow13), Write(arrow23), Write(arrow33))
        self.wait(2)
        self.play(FadeOut(arrow13), FadeOut(arrow33))
        self.wait(2)

class Illustrate(Scene):
    def construct(self):
        block_blue = RoundedRectangle(height=1.5, width=2, color=BLUE)
        block_blue.set_fill(color=BLUE, opacity=0.5)
        block_green = RoundedRectangle(height=1.5, width=2, color=GREEN)
        block_green.set_fill(color=GREEN, opacity=0.5)
        block_yellow = RoundedRectangle(height=1.5, width=2, color=YELLOW)
        block_yellow.set_fill(color=YELLOW, opacity=0.5)
        block_purple = RoundedRectangle(height=1.5, width=2, color=PURPLE)
        block_purple.set_fill(color=PURPLE, opacity=0.5)
        block_blue.shift(RIGHT, RIGHT, RIGHT, RIGHT, UP, UP, UP)
        block_green.shift(RIGHT, RIGHT, RIGHT, RIGHT, UP)
        block_yellow.shift(RIGHT, RIGHT, RIGHT, RIGHT, DOWN)
        block_purple.shift(RIGHT, RIGHT, RIGHT, RIGHT, DOWN, DOWN, DOWN)

        text1 = Tex("Codeword", font_size=64)
        text1.shift(LEFT, LEFT, LEFT)
        text2 = MathTex("(Length = {l_i})", font_size=48)
        text2.shift(LEFT, LEFT, LEFT, DOWN)

        text = Text("N2")
        text.scale(0.8)
        text.move_to(block_blue)
        block_blue = VGroup(block_blue, text)

        text = Text("N3")
        text.scale(0.8)
        text.move_to(block_green)
        block_green = VGroup(block_green, text)

        text = Text("N4")
        text.scale(0.8)
        text.move_to(block_yellow)
        block_yellow = VGroup(block_yellow, text)

        text = Text("N5")
        text.scale(0.8)
        text.move_to(block_purple)
        block_purple = VGroup(block_purple, text)

        gr = VGroup(text1, text2, block_blue, block_green, block_yellow, block_purple)
        self.play(gr.animate)
        self.wait(1)

        arrow1 = Arrow(text1.get_right(), block_blue.get_left())
        arrow2 = Arrow(text1.get_right(), block_green.get_left())
        arrow3 = Arrow(text1.get_right(), block_yellow.get_left())
        arrow4 = Arrow(text1.get_right(), block_purple.get_left())
        self.play(Create(arrow1), Create(arrow2), Create(arrow3), Create(arrow4))

        self.wait(2)

class Decode(Scene):
    def construct(self):
        text1 = Tex("Codeword", font_size=64)
        text1.shift(LEFT, LEFT, LEFT, LEFT, LEFT, UP, UP)
        text2 = MathTex("(Length = {l_j})", font_size=48)
        text2.shift(LEFT, LEFT, LEFT, LEFT, LEFT, UP)

        block_blue = RoundedRectangle(height=1.5, width=2, color=BLUE)
        block_blue.set_fill(color=BLUE, opacity=0.5)
        block_blue.shift(LEFT, LEFT, LEFT, LEFT, LEFT, DOWN, DOWN)
        text = MathTex(r"{C_i}")
        text.scale(0.8)
        text.move_to(block_blue)
        block_blue = VGroup(block_blue, text)

        block_decoder = Rectangle(color=GREY)
        block_decoder.set_fill(color=GREY, opacity=0.5)

        text = Tex("Decoder", font_size=72)
        text.scale(0.8)
        text.move_to(block_decoder)
        block_decoder = VGroup(block_decoder, text)
        arrow = Arrow(block_blue.get_right(), block_decoder.get_left())
        arrow1 = Arrow(text1.get_right(), block_decoder.get_left())

        block_red = RoundedRectangle(height=1.5, width=2, color=RED_C)
        block_red.set_fill(color=RED_C, opacity=0.35)
        block_red.shift(RIGHT, RIGHT, RIGHT, RIGHT, RIGHT)
        text = MathTex(r"{d_i}")
        text.scale(0.8)
        text.move_to(block_red)
        block_red = VGroup(block_red, text)
        arrow2 = Arrow(block_decoder.get_right(), block_red.get_left())

        tex = MathTex(
            r"\psi_i : \{0, 1\}^{|C_i|} \times \{0, 1\}^{\sum_{j\neq i} l_j} \rightarrow \{0, 1\}^{|D_i|}",
            font_size=36,
        )
        tex.shift(DOWN, DOWN)
        self.play(Create(text1), Create(text2), Create(block_blue), run_time=2)
        self.play(Create(arrow), Create(arrow1), run_time=2)
        self.play(Create(block_decoder), Create(tex), run_time=2)
        self.play(Create(arrow2))
        self.play(Create(block_red), run_time=2)
        self.wait(2)

class DecodeandMatch(Scene):
    def construct(self):
        block_blue = RoundedRectangle(height=1.5, width=2, color=BLUE)
        block_blue.set_fill(color=BLUE, opacity=0.5)
        block_green = RoundedRectangle(height=1.5, width=2, color=GREEN)
        block_green.set_fill(color=GREEN, opacity=0.5)
        block_yellow = RoundedRectangle(height=1.5, width=2, color=YELLOW)
        block_yellow.set_fill(color=YELLOW, opacity=0.5)
        block_purple = RoundedRectangle(height=1.5, width=2, color=PURPLE)
        block_purple.set_fill(color=PURPLE, opacity=0.5)
        block_blue.shift(RIGHT, RIGHT, RIGHT, UP, UP, UP)
        block_green.shift(RIGHT, RIGHT, RIGHT, UP)
        block_yellow.shift(RIGHT, RIGHT, RIGHT, DOWN)
        block_purple.shift(RIGHT, RIGHT, RIGHT, DOWN, DOWN, DOWN)

        text1 = Tex("Codeword", font_size=64)
        text1.shift(LEFT, LEFT, LEFT)
        text2 = MathTex("(Length = {l_i})", font_size=48)
        text2.shift(LEFT, LEFT, LEFT, DOWN)

        text = Text("N2")
        text.scale(0.8)
        text.move_to(block_blue)
        block_blue = VGroup(block_blue, text)

        text = Text("N3")
        text.scale(0.8)
        text.move_to(block_green)
        block_green = VGroup(block_green, text)

        text = Text("N4")
        text.scale(0.8)
        text.move_to(block_yellow)
        block_yellow = VGroup(block_yellow, text)

        text = Text("N5")
        text.scale(0.8)
        text.move_to(block_purple)
        block_purple = VGroup(block_purple, text)

        gr = VGroup(text1, text2, block_blue, block_green, block_yellow, block_purple)

        arrow11 = Arrow(text1.get_right(), block_blue.get_left())
        arrow21 = Arrow(text1.get_right(), block_green.get_left())
        arrow31 = Arrow(text1.get_right(), block_yellow.get_left())
        arrow41 = Arrow(text1.get_right(), block_purple.get_left())
        gr = VGroup(gr, arrow11, arrow21, arrow31, arrow41)
        gr.shift(LEFT, LEFT, LEFT * 0.5)
        self.play(gr.animate)
        self.wait(2)
        t2 = MathTex("{d_2}", font_size=64)
        t3 = MathTex("{d_3}", font_size=64)
        t4 = MathTex("{d_4}", font_size=64)
        t5 = MathTex("{d_5}", font_size=64)
        t2.shift(RIGHT, RIGHT, RIGHT, RIGHT, UP, UP, UP)
        t3.shift(RIGHT, RIGHT, RIGHT, RIGHT, UP)
        t4.shift(RIGHT, RIGHT, RIGHT, RIGHT, DOWN)
        t5.shift(RIGHT, RIGHT, RIGHT, RIGHT, DOWN, DOWN, DOWN)
        arrow1 = Arrow(block_blue.get_right(), t2.get_left())
        arrow2 = Arrow(block_green.get_right(), t3.get_left())
        arrow3 = Arrow(block_yellow.get_right(), t4.get_left())
        arrow4 = Arrow(block_purple.get_right(), t5.get_left())
        self.play(Create(arrow1), Create(arrow2), Create(arrow3), Create(arrow4))
        self.play(Create(t2), Create(t3), Create(t4), Create(t5))
        self.wait(2)
        t21 = MathTex(r"\neq {D_2}", font_size=64)
        t31 = MathTex(r"= {D_3}", font_size=64)
        t41 = MathTex(r"\neq {D_4}", font_size=64)
        t51 = MathTex(r"\neq {D_5}", font_size=64)
        t21.next_to(t2, RIGHT)
        t31.next_to(t3, RIGHT)
        t41.next_to(t4, RIGHT)
        t51.next_to(t5, RIGHT)
        group = VGroup(t3, t31)
        self.play(Create(t21), Create(t31), Create(t41), Create(t51))
        self.wait(2)
        self.remove(
            arrow11,
            arrow31,
            arrow41,
            block_blue,
            block_yellow,
            block_purple,
            t2,
            t4,
            t5,
            arrow1,
            arrow3,
            arrow4,
            t21,
            t41,
            t51,
        )
        transform_block = RoundedRectangle(height=1.5, width=2, color=GREEN)
        transform_block.set_fill(color=GREEN, opacity=0.5)
        text = Text("N3")
        text.scale(0.8)
        text.move_to(transform_block)
        transform_block = VGroup(transform_block, text)
        transform_group = group
        transform_group.shift(DOWN)
        arrow_new1 = Arrow(text1.get_right(), transform_block.get_left())
        arrow_new2 = Arrow(transform_block.get_right(), transform_group.get_left())
        self.play(
            Transform(block_green, transform_block),
            Transform(group, transform_group),
            Transform(arrow21, arrow_new1),
            Transform(arrow2, arrow_new2),
        )
        self.wait(1)
        decodeText = MathTex(
            "Using\\ the\\ equation," r"\psi_3(C_3, \{\phi_j(C_j) : j \neq 2\}) = D_3"
        )
        decodeText.shift(UP, UP, LEFT, LEFT * 0.25)
        Info = Tex("Thus, Information is transferred successfully")
        Info.shift(DOWN, DOWN, DOWN * 0.5, LEFT, LEFT)
        self.play(FadeIn(decodeText), FadeIn(Info))
        self.wait(2)

class Load(Scene):
    def construct(self):
        text = Tex("The communication load of the aforementioned scheme is defined as the total number of bits communicated, i.e.,").scale(0.8)
        text.shift(UP*1.5)
        eqn = Tex(r"$L(\Phi ,\Psi )\triangleq \sum_{i\in [K]}l_{i}$")
        Gr = VGroup(text,eqn)
        self.play(Write(text))
        self.play(Write(eqn))
        text = Tex("The optimal communication load is then denoted by").scale(0.8)
        eqn = Tex(r"$L^{*}\triangleq \underset{\Phi ,\Psi }{min} L(\Phi ,\Psi )$")
        text.shift(DOWN)
        eqn.shift(DOWN*2)
        self.play(Write(text))
        self.play(Write(eqn))
        Gr=VGroup(Gr,text,eqn)
        self.wait(3)
        self.play(FadeOut(Gr))

class converse(Scene):
    def construct(self):
        text = Text("Converse for data exchange problem", font_size=36)
        self.play(text.animate)
        self.wait(15)
        self.play(text.animate.shift(LEFT * 3, UP * 3.5), run_time=2)
        
        tex = MathTex(
            r"a_{P}^{Q} \triangleq |(\cap_{i\in P}D_{i})\cap (\cap_{j\in Q}C_{j})\setminus (\cup_{j\notin Q}C_{j})\cup(\cup_{i\notin P}D_{i})|",
            font_size=54,
        )
        self.play(FadeIn(tex))
        self.wait(10)
        self.play(tex.animate.shift(UP * 2))
        self.wait(1)

        tex1 = MathTex(r"a_{P}^{Q} = 0")
        text1 = Text("under following conditions: ", font_size=36)
        text1.next_to(tex1)
        tex1 = VGroup(tex1, text1)
        tex1.shift(LEFT * 3)
        tex2 = MathTex("(I) " r"P\cap Q \neq \phi")

        tex3 = MathTex("(II) " r"Q = \phi")

        tex2.shift(DOWN, LEFT, LEFT, LEFT, LEFT)
        tex3.shift(DOWN, RIGHT, RIGHT, RIGHT)
        equation = VGroup(tex1, tex2, tex3)
        self.play(Write(equation))
        self.wait(10)

class Theorem1(Scene):
    def construct(self):
        text = Text("Theorem 1:")
        text.shift(LEFT, LEFT, LEFT, LEFT, LEFT, UP, UP)
        self.play(Write(text))
        tex = MathTex(
            r"L^*\geq \sum_{P\subset [K]}\sum_{Q\subset [K]\setminus P} \frac{|P|}{|P|+|Q|-1}a_{P}^{Q}"
        )
        self.play(Write(tex))
        self.wait(3)
        self.remove(text)
        self.remove(tex)
        text2 = Text("Corollary 1:")
        text2.shift(LEFT, LEFT, LEFT, LEFT, LEFT, UP, UP, UP * 1.5)
        t1 = Text("Let").scale(0.8)
        t1.shift(LEFT, LEFT, LEFT, LEFT, LEFT * 1.25, LEFT, UP, UP, UP * 0.5)
        t2 = MathTex(
            r"n(p, q) \triangleq \sum_{\substack{P,Q\subseteq[K]\\|P|=p,|Q|=q,P\cap Q=\emptyset}} a^{Q}_{P}"
        )
        t2.shift(UP * 1.5)
        t3 = Text(
            "denote the total number of bits present exactly in q nodes and\ndemanded exactly by p (other) nodes."
        ).scale(0.65)
        t3.shift(LEFT * 0.75)
        t4 = Text("Then").scale(0.8)
        t4.shift(LEFT, LEFT, LEFT, LEFT, LEFT, LEFT, DOWN)
        t5 = MathTex(
            r"L^* \geq \sum_{p=1}^{K-1} \sum_{q=1}^{K-p} \frac{p}{p+q-1} n(p, q)"
        )
        t5.shift(DOWN, DOWN * 1.25)
        tex2 = VGroup(t1, t2, t3, t4, t5)
        self.play(Transform(text, text2), Transform(tex, tex2))
        self.wait(3)

class Theorem1Example(Scene):
    def construct(self):
        tex1 = MathTex(r"a_{\{2\}}^{\{1\}} : D_1 \in N_2")
        tex1.shift(UP * 1.5)
        tex2 = MathTex(r"a_{\{1\}}^{\{2\}} : D_2 \in N_1")
        result = MathTex(r"L^* \geq a_{\{2\}}^{\{1\}} + a_{\{1\}}^{\{2\}}")
        result.shift(DOWN * 1.5)
        group = VGroup(tex1, tex2, result)
        self.play(Write(group))
        self.wait(20)
        self.play(group.animate.shift(LEFT * 4))
        self.wait(2)

        blockC1 = Rectangle(height=1.2, width=1.1, color=WHITE)
        blockD1 = Rectangle(height=1.2, width=1.1, color=WHITE)
        N2 = Rectangle(height=1.2, width=1.1, color=WHITE)
        blockC1.shift(UP * 0.6)
        blockD1.shift(DOWN * 0.6)
        N2.shift(RIGHT * 2)
        text = MathTex(r"{C_1}", font_size=48)
        text.move_to(blockC1)
        blockC1 = VGroup(blockC1, text)
        text = MathTex(r"{D_1}", font_size=48)
        text.move_to(blockD1)
        blockD1 = VGroup(blockD1, text)
        text = MathTex(r"{N_2}", font_size=48)
        text.move_to(N2)
        N2 = VGroup(N2, text)
        tex12 = MathTex(r"a_{\{2\}}^{\{1\}}")
        tex12.shift(UP * 1.75, RIGHT)

        block1 = VGroup(tex12, blockC1, blockD1, N2)
        block1.shift(RIGHT * 3.5, UP * 1.5)
        block1.flip()

        blockC2 = Rectangle(height=1.2, width=1.1, color=WHITE)
        blockD2 = Rectangle(height=1.2, width=1.1, color=WHITE)
        N1 = Rectangle(height=1.2, width=1.1, color=WHITE)
        blockC2.shift(UP * 0.6)
        blockD2.shift(DOWN * 0.6)
        N1.shift(RIGHT * 2)
        text = MathTex(r"{C_2}", font_size=48)
        text.move_to(blockC2)
        blockC2 = VGroup(blockC2, text)
        text = MathTex(r"{D_2}", font_size=48)
        text.move_to(blockD2)
        blockD2 = VGroup(blockD2, text)
        text = MathTex(r"{N_1}", font_size=48)
        text.move_to(N1)
        N1 = VGroup(N1, text)
        tex22 = MathTex(r"a_{\{1\}}^{\{2\}}")
        tex22.shift(UP * 1.75, RIGHT)

        block2 = VGroup(tex22, blockC2, blockD2, N1)
        block2.shift(RIGHT * 3.5, DOWN * 2)
        block2.flip()
        block = VGroup(block1, block2)
        block.shift(LEFT, LEFT * 0.5)
        self.play(block.animate.flip())
        arrow1 = Arrow(blockD1.get_left(), N2.get_right())
        arrow2 = Arrow(blockD2.get_left(), N1.get_right())
        block11 = VGroup(blockC1, blockD1)
        block21 = VGroup(blockC2, blockD2)
        self.play(
            block11.animate.shift(LEFT, LEFT * 0.5),
            block21.animate.shift(LEFT, LEFT * 0.5),
            N1.animate.shift(RIGHT, RIGHT * 0.5),
            N2.animate.shift(RIGHT, RIGHT * 0.5),
        )
        self.play(Write(arrow1), Write(arrow2))
        self.wait(15)
        rectangle = Rectangle(height=1,width=4)
        rectangle.move_to(result)
        self.play(Create(rectangle))
        self.wait(1)

class GeneralStructure(Scene):
    def construct(self):
        text1 = Text("1)  Applying Theorem 1")
        text2 = Text("2)  Symmetrization step")
        text3 = Text("3)  Refine the averaged bound")
        text1.shift(LEFT, LEFT, LEFT, UP, UP)
        text2.shift(LEFT, LEFT)
        text3.shift(DOWN, DOWN)
        self.wait(2)
        self.play(Write(text1))
        self.wait(12)
        self.play(Write(text2))
        self.wait(12)
        self.play(Write(text3))
        self.wait(17)

class Computing(Scene):
    def construct(self):
        text = Text("The described scheme is used to recover lower bound for the following",slant=ITALIC)
        text.shift(LEFT * 4.5, UP * 2.5)
        text1 = Text(
            "1) Coded Caching\n\n2) Coded Data Shuffling\n\n3) Coded Computing"
        )
        text1.shift(LEFT)
        text = VGroup(text, text1)
        self.play(FadeIn(text))
        self.wait(10)
        text1 = Text("Coded Distributed Computing")
        text1 = Transform(text, text1)
        self.play(text1)
        self.wait(4)
        self.play(FadeOut(text))
        self.wait(6)
        m1 = Text("M1", font="Bradley Hand ITC", font_size=48)
        m1.shift(LEFT * 5, UP * 3)
        m2 = Text("M2", font="Bradley Hand ITC", font_size=48)
        m2.shift(LEFT * 2, UP * 3)
        mk = Text("MK", font="Bradley Hand ITC", font_size=48)
        mk.shift(RIGHT * 5, UP * 3)
        Gr = VGroup(m1, m2, mk)
        self.play(Write(m1), Write(m2), Write(mk))
        self.wait(2)
        N11 = Rectangle(height=1, width=2)
        N11.shift(LEFT * 5, UP * 1.5)
        text = Text("Node 1").scale(0.7)
        text.move_to(N11)
        N11 = VGroup(N11, text)
        N21 = Rectangle(height=1, width=2)
        N21.shift(LEFT * 2, UP * 1.5)
        text = Text("Node 2").scale(0.7)
        text.move_to(N21)
        N21 = VGroup(N21, text)
        N31 = Rectangle(height=1, width=2)
        N31.shift(RIGHT * 5, UP * 1.5)
        text = Text("Node K").scale(0.7)
        text.move_to(N31)
        N31 = VGroup(N31, text)
        arrow1 = Arrow(start=[-5, 3, 0], end=[-5, 1.75, 0])
        arrow2 = Arrow(start=[-2, 3, 0], end=[-2, 1.75, 0])
        arrow3 = Arrow(start=[5, 3, 0], end=[5, 1.75, 0])
        dashedLine1 = DashedLine(
            start=[-0.5, 1.5, 0], end=[3.5, 1.5, 0], dashed_ratio=0.2
        )

        Gr = VGroup(Gr, N11, N21, N31, arrow1, arrow2, arrow3, dashedLine1)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.play(FadeIn(N11), FadeIn(N21), FadeIn(N31), FadeIn(dashedLine1))
        self.wait(2)

        N11 = Rectangle(height=0.5, width=2)
        N11.shift(LEFT * 5)
        text = MathTex(r"\phi_{1} (.)").scale(0.7)
        text.move_to(N11)
        N11 = VGroup(N11, text)
        N21 = Rectangle(height=0.5, width=2)
        N21.shift(LEFT * 2)
        text = MathTex(r"\phi_{2} (.)").scale(0.7)
        text.move_to(N21)
        N21 = VGroup(N21, text)
        N31 = Rectangle(height=0.5, width=2)
        N31.shift(RIGHT * 5)
        text = MathTex(r"\phi_{K} (.)").scale(0.7)
        text.move_to(N31)
        N31 = VGroup(N31, text)
        arrow1 = Arrow(start=[-5, 1.2, 0], end=[-5, -0.0005, 0])
        arrow2 = Arrow(start=[-2, 1.2, 0], end=[-2, -0.0005, 0])
        arrow3 = Arrow(start=[5, 1.2, 0], end=[5, -0.0005, 0])
        tex1 = MathTex(r"\nu_{1}:\mathit{Q,M_{1}}")
        tex2 = MathTex(r"\nu_{2}:\mathit{Q,M_{2}}")
        tex3 = MathTex(r"\nu_{k}:\mathit{Q,M_{K}}")
        tex1.move_to(arrow1, LEFT).scale(0.6).shift(LEFT * 0.25)
        tex2.move_to(arrow2, LEFT).scale(0.6).shift(LEFT * 0.25)
        tex3.move_to(arrow3, RIGHT).scale(0.6).shift(RIGHT * 0.25)
        dashedLine2 = DashedLine(start=[-0.5, 0, 0], end=[3.5, 0, 0], dashed_ratio=0.2)
        Gr = VGroup(
            Gr, N11, N21, N31, arrow1, arrow2, arrow3, tex1, tex2, tex3, dashedLine2
        )
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.play(FadeIn(N11), FadeIn(N21), FadeIn(N31), FadeIn(dashedLine2))
        self.play(Write(tex1), Write(tex2), Write(tex3))
        self.wait(2)

        text1 = Tex("$X_{1}$")
        text1.shift(LEFT * 5, DOWN * 1)
        text2 = Tex("$X_{2}$")
        text2.shift(LEFT * 2, DOWN * 1)
        text3 = Tex("$X_{K}$")
        text3.shift(RIGHT * 5, DOWN * 1)
        arrow1 = Arrow(
            start=[-5, 0, 0], end=[-5, -1, 0], max_tip_length_to_length_ratio=0.4
        )
        arrow2 = Arrow(
            start=[-2, 0, 0], end=[-2, -1, 0], max_tip_length_to_length_ratio=0.4
        )
        arrow3 = Arrow(
            start=[5, 0, 0], end=[5, -1, 0], max_tip_length_to_length_ratio=0.4
        )
        Gr = VGroup(Gr, arrow1, arrow2, arrow3, text1, text2, text3)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.play(FadeIn(text1), FadeIn(text2), FadeIn(text3))
        self.wait(2)

        N11 = Rectangle(height=1, width=2)
        N11.shift(LEFT * 5, DOWN * 2.75)
        text = Text("Node 1").scale(0.7)
        text.move_to(N11)
        N11 = VGroup(N11, text)
        N21 = Rectangle(height=1, width=2)
        N21.shift(LEFT * 2, DOWN * 2.75)
        text = Text("Node 2").scale(0.7)
        text.move_to(N21)
        N21 = VGroup(N21, text)
        N31 = Rectangle(height=1, width=2)
        N31.shift(RIGHT * 5, DOWN * 2.75)
        text = Text("Node K").scale(0.7)
        text.move_to(N31)
        N31 = VGroup(N31, text)
        self.play(FadeIn(N11), FadeIn(N21), FadeIn(N31))
        Gr = VGroup(Gr, N11, N21, N31)
        self.wait(2)
        arrow1 = Arrow(
            start=[-5, -1.2, 0],
            end=[-2, -2.2, 0],
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.1,
        )
        arrow2 = Arrow(
            start=[-5, -1.2, 0],
            end=[5.2, -2.18, 0],
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.03,
        )
        arrow3 = Arrow(
            start=[-2, -1.2, 0],
            end=[-5, -2.2, 0],
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.1,
        )
        arrow4 = Arrow(
            start=[-2, -1.2, 0],
            end=[5.1, -2.18, 0],
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.05,
        )
        arrow5 = Arrow(
            start=[5, -1.2, 0],
            end=[-5, -2.2, 0],
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.03,
        )
        arrow6 = Arrow(
            start=[5, -1.2, 0],
            end=[-2, -2.2, 0],
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.04,
        )
        Gr = VGroup(Gr, arrow1, arrow2, arrow3, arrow4, arrow5, arrow6)
        self.play(Write(arrow1), Write(arrow2))
        self.play(Write(arrow3), Write(arrow4))
        self.play(Write(arrow5), Write(arrow6))
        self.wait(2)

        arrow1 = Arrow(
            start=[-5, -3, 0], end=[-5, -4, 0], max_tip_length_to_length_ratio=0.4
        )
        arrow2 = Arrow(
            start=[-2, -3, 0], end=[-2, -4, 0], max_tip_length_to_length_ratio=0.4
        )
        arrow3 = Arrow(
            start=[5, -3, 0], end=[5, -4, 0], max_tip_length_to_length_ratio=0.4
        )
        Gr = VGroup(Gr, arrow1, arrow2, arrow3)
        self.play(Create(arrow1), Create(arrow2), Create(arrow3))
        self.wait(2)
        Gr1 = Gr.copy().scale(0.8).shift(RIGHT * 1.5)
        self.play(Transform(Gr, Gr1))
        self.wait(2)
        rectangle1 = DashedVMobject(Rectangle(width=13, height=1.5), num_dashes=500)
        rectangle1.shift(UP)
        text11 = Text(" Map \nPhase").scale(0.8)
        text11.shift(UP, LEFT * 5)
        self.play(Create(rectangle1))
        self.play(Write(text11))
        rectangle2 = DashedVMobject(Rectangle(width=13, height=1.5), num_dashes=500)
        rectangle2.shift(DOWN * 0.6)
        text22 = Text("Shuffle\n Phase ").scale(0.8)
        text22.shift(LEFT * 5, DOWN * 0.6)
        self.play(Create(rectangle2))
        self.play(Write(text22))
        rectangle3 = DashedVMobject(Rectangle(width=13, height=1.5), num_dashes=500)
        rectangle3.shift(DOWN * 2.25)
        text33 = Text("Reduce\n Phase ").scale(0.8)
        text33.shift(LEFT * 5, DOWN * 2.25)
        self.play(Create(rectangle3))
        self.play(Write(text33))
        self.wait(2)

        self.remove(rectangle2,text22,rectangle3,text33)
        self.wait(38)
        self.add(rectangle2,text22,rectangle3,text33)

        self.remove(rectangle1,text11,rectangle2,text22)
        self.wait(55)
        self.add(rectangle1,text11,rectangle2,text22)

        self.remove(rectangle1,text11,rectangle3,text33)
        self.wait(37)
        self.add(rectangle1,text11,rectangle3,text33)

        Gr = VGroup(Gr,rectangle1,text11,rectangle2,text22,rectangle3,text33)
        # Gr = VGroup(Gr,rectangle3,text33)

        self.play(FadeOut(Gr))

        text = Tex(
            "The minimum communication load "
            + r"$L_{dc}^{*}$"
            + " incurred by a distributed computing system of K nodes for a given computation load r, where every reduce function is computed at exactly one node and each node computes "
            + r"$\frac{W}{K}$"
            + " reduce functions, is bounded as"
        )
        text.scale(0.8).shift(UP)
        eqn = Tex(
            r"$\frac{L_{dc}^{*}}{WNT} \geq \frac{1}{r}\left ( 1-\frac{r}{K} \right )$"
        )
        eqn.shift(DOWN).scale(1.5)
        self.play(Write(text))
        self.play(Write(eqn))
        Gr1 = VGroup(text, eqn)
        self.wait(24)
        text = Text("Refining the bound using convexity and setting constraints",weight=BOLD).scale(0.6)
        text1 = Tex("Using definition of " + r"$L_{dc}^{*}$" + ", noting that " + r"$\frac{K-j}{j}$" + " is a convex decreasing function of " + r"$j$" + "and that " + r"$\frac{\sum_{j=1}^{K}\tilde{a}_{M}^{j}}{N} = 1$" + ", we have that").scale(0.8)
        eqn = Tex(r"$\frac{L_{dc}^{*}}{WNT}\geq \frac{1}{K}\frac{K-\sum_{j=1}^{K}\frac{j\tilde{a}_{M}^{j}}{N}}{\sum_{j=1}^{K}\frac{j\tilde{a}_{M}^{j}}{N}}=\frac{1}{r}(1-\frac{r}{K})$").scale(1.2)
        text.shift(UP*2.5 + LEFT)
        text1.shift(UP)
        eqn.shift(DOWN*1)
        Gr2 = VGroup(text,text1,eqn)
        self.play(Transform(Gr1,Gr2))
        self.wait(5)
        Pro = Text("Proposition 2", weight=BOLD)
        Pro.shift(UP * 2.5, LEFT * 4.5)
        text = Tex(
            "The communication load corresponding to a map function assignment M when each reduce function has to be computed at s nodes is lower bounded as"
        )
        text.scale(0.8).shift(UP)
        eqn = Tex(
            r"$\frac{L_{M}(s)}{WNT}\geq \sum_{j=1}^{K}\frac{\tilde{a}_{M}^{j}}{N}\sum_{l=max(0,s-j)}^{min(K-j,s)}\frac{\binom{K-j}{l}\binom{j}{s-l}}{\binom{K}{s}}\frac{l}{l+j-1}$"
        )
        eqn.shift(DOWN)
        Gr3 = VGroup(Pro, text, eqn)
        self.play(Transform(Gr1, Gr3))
        self.wait(4)
        self.play(FadeOut(Gr1))


class Conclusion(Scene):
    def construct(self):
        text = Text("CONCLUSION", weight=BOLD)
        text.shift(UP * 3 + LEFT * 4.5)
        self.play(Write(text))
        text1 = Tex(
            "We have presented an information theoretic converse result for a generic data exchange problem, where the terminals contain some data in their local storage and want other data available at the local storage of other nodes." 
            + "The main result of this paper is the derivation of a converse to the data exchange problem, which provides a lower bound on the optimal communication load for various scenarios related to coded caching, computing, and shuffling."
        ).scale(0.8)

        self.play(Write(text1))
        self.wait(28)
        gr = VGroup(text, text1)
        self.play(FadeOut(gr))


class TheEnd(Scene):
    def construct(self):
        text = Text("Thank You :)", font="CommercialScript BT").scale(2)
        # self.play(Create(text))
        self.play(Write(text), run_time=2)
        self.wait(2)

class Play(Scene):
    def construct(self):
        Introduction.construct(self)
        SingleNode.construct(self)
        self.clear()
        Encode.construct(self)
        self.clear()
        Illustrate.construct(self)
        self.clear()
        Decode.construct(self)
        self.clear()
        DecodeandMatch.construct(self)
        self.clear()
        Illustrate2.construct(self)
        self.clear()
        Load.construct(self)
        converse.construct(self)
        self.clear()
        Theorem1.construct(self)
        self.clear()
        Theorem1Example.construct(self)
        self.clear()
        GeneralStructure.construct(self)
        self.clear()
        Computing.construct(self)
        Conclusion.construct(self)
        TheEnd.construct(self)